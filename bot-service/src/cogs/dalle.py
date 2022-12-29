import discord
import logging

from . import openai_client
from . import voucher_service_client as vsc
from openai.error import InvalidRequestError
from discord.ext import commands
from discord import app_commands


class Dalle(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = openai_client.OpenAIClient()

    @commands.hybrid_command(description="Generate an image.")
    @app_commands.describe(prompt="Prompt provided to the image generation model.")
    async def generate(self, context: commands.Context, prompt: str):
        try:
            await context.defer()
            vouchers = vsc.get_vouchers(context.author.id)
            valid_vouchers = [v for v in vouchers if v["credits"] > 0]
            
            if (valid_vouchers):
                image_url = self.client.create_image(prompt)
                await context.send(image_url)
                vsc.subtract_credits(valid_vouchers[0]["voucher_id"])
            else:
                await context.send("You have no credits. Please purchase credits to use DALL-E.")

        except InvalidRequestError as err:
            logging.error(err)
            await context.send(str(err))

        except Exception as e:
            logging.error(e)
            await context.send("DALL-E is currently unavailable. Please try again in a few minutes.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Dalle(bot))

