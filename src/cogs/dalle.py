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

    @app_commands.command(description="Generate an image.")
    async def generate(self, interaction: discord.Interaction, description: str):
        try:
            await interaction.response.defer()
            image_url = self.client.create_image(description)
            await interaction.followup.send(image_url)
        except InvalidRequestError as err:
            logging.error(err)
            await interaction.followup.send(str(err))
        except Exception as e:
            logging.error(e)
            await interaction.followup.send("DALL-E is currently unavailable. Please try again in a few minutes.")


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
