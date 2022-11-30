import os
import discord
import logging
import openai

from tenacity import (
    retry,
    stop_after_attempt,
    retry_if_not_exception_type,
    stop_after_delay,
    wait_exponential
)
from openai.error import InvalidRequestError
from discord.ext import commands
from discord import app_commands

class Dalle(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = OpenAIClient()

    @commands.hybrid_command(description="Generate an image.")
    @app_commands.describe(prompt="Prompt provided to the image generation model.")
    async def generate(self, context: commands.Context, prompt: str):
        try:
            await context.defer()
            image_url = self.client.create_image(prompt)
            await context.send(image_url)
        except InvalidRequestError as err:
            logging.error(err)
            await context.send(str(err))
        except Exception as e:
            logging.error(e)
            await context.send("DALL-E is currently unavailable. Please try again in a few minutes.")


class OpenAIClient:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @retry(
        wait=wait_exponential(min=1, max=10), 
        stop=(stop_after_attempt(5) | stop_after_delay(30)),
        retry=retry_if_not_exception_type(openai.error.InvalidRequestError))
    def create_image(self, prompt: str):
        response = openai.Image.create(prompt=prompt)
        image_url = response["data"][0]["url"]
        return image_url


async def setup(bot: commands.Bot):
    await bot.add_cog(Dalle(bot))
