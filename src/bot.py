import os
import discord

from openai.error import InvalidRequestError
from intents import intents
from openai_client import OpenAIClient
from discord.ext import commands
from dotenv import load_dotenv

def run():

    load_dotenv()
    openai_client = OpenAIClient()
    bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

    @bot.command(aliases=['dall-e'], help='Create an image with DALL-E.')
    async def dalle(context, *, prompt):
        try:
            image_url = openai_client.create_image(prompt)
            await context.send(image_url)
        except InvalidRequestError as err:
            await context.send(str(err))
        except Exception as e:
            await context.send("DALL-E is currently unavailable. Please try again in a few minutes.")
    
    @bot.command(help='Check your remaining DALL-E credits.')
    async def credits(context):
        await context.send("You have 13 credits remaining.")

    @bot.event
    async def on_command_error(context, error):
        if hasattr(context.command, 'on_error'):
            return

        if isinstance(error, commands.CommandNotFound):
            return

    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)

def main():
    run()

if '__main__' == __name__:
    main()
