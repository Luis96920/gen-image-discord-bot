from discord import Intents
from discord.ext import commands

class DalleBot(commands.Bot):

    def __init__(self):
        intents = Intents.default()
        intents.typing = False
        intents.presences = False
        intents.message_content = True
        super().__init__(command_prefix="/", intents=intents)
        
    async def setup_hook(self):
        await self.load_extension("cogs.credits")
        await self.load_extension("cogs.dalle")
        await self.tree.sync()

