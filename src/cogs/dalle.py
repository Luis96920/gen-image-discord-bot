import discord

from openai.error import InvalidRequestError
from openai_client import OpenAIClient
from discord.ext import commands
from discord import app_commands

class Dalle(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description='Generate an image.')
    async def generate(self, interaction: discord.Interaction, prompt: str):
        try:
            await interaction.response.defer()
            image_url = openai_client.create_image(prompt)
            await interaction.followup.send(image_url)
        except InvalidRequestError as err:
            logging.error(err)
            await interaction.response.send_message(str(err))
        except Exception as e:
            logging.error(e)
            await interaction.response.send_message("DALL-E is currently unavailable. Please try again in a few minutes.")

async def setup(bot: commands.bot):
    await bot.add_cog(Dalle(bot))

