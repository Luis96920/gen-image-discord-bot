import discord
from discord.ext import commands

class DalleBot(commands.Bot):

    def __init__(self):
        intents = discord.Intents.default()
        intents.typing = False
        intents.guild_typing = False
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        
    async def setup_hook(self):
        await self.load_extension("cogs.credits")
        await self.load_extension("cogs.dalle")
        await self.load_extension("cogs.admin")

