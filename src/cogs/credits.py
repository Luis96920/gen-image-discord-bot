import discord

from discord import app_commands
from discord.ext import commands

class Credits(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="Check your remaining credits.")
    async def credits(self, interaction: discord.Interaction):
        await interaction.response.send_message("You have 10 credits remaining.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))

