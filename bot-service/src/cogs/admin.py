import os
import discord
import logging

from discord.ext import commands
from typing import Literal

class Admin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    @commands.guild_only()
    async def sync(self, context: commands.Context, spec: Literal["test", "reset", "deploy"]):
        if context.guild.id != int(os.getenv("ADMIN_GUILD_ID")):
            return

        # Test commands in the admin guild
        if spec == "test":
            context.bot.tree.copy_global_to(guild=context.guild)
            synced = await context.bot.tree.sync(guild=context.guild)
            logging.info(f"Synced {len(synced)} commands in test guild")

        # Clear commands in the admin guild and sync back to original state 
        elif spec == "reset":
            context.bot.tree.clear_commands(guild=context.guild)
            await context.bot.tree.sync(guild=context.guild)
            logging.info(f"Reset commands in test guild")

        # Deploy commands globally to all guilds
        elif spec == "deploy":
            synced = await context.bot.tree.sync()
            logging.info(f"Synced {len(synced)} commands globally")

        return

async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))

