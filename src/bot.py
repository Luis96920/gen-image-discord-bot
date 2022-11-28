import os
import discord
import logging

from openai.error import InvalidRequestError
from intents import intents
from openai_client import OpenAIClient
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from discord_client import DiscordClient

def run():
    load_dotenv()
    openai_client = OpenAIClient()
    client = DiscordClient(intents=intents)

    @client.tree.command(description='Generate an image.')
    async def generate(interaction: discord.Interaction, prompt: str):
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

    @client.tree.command(description='Check your available credits.')
    async def credits(interaction: discord.Interaction):
        await interaction.response.send_message("You have 13 credits remaining.")

    TOKEN = os.getenv('DISCORD_TOKEN')
    client.run(TOKEN)

def main():
    run()

if '__main__' == __name__:
    main()
