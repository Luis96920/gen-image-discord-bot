import sys
from discord.ext import commands
from . import voucher_service_client as vsc

class Credits(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(description="Check your remaining credits.")
    async def credits(self, context: commands.Context):
        credits = vsc.get_credits(context.author.id)

        if credits > 1:
            await context.send(f"You have {credits} credits remaining.")
        elif credits == 1:
            await context.send(f"You have {credits} credit remaining.")
        else:
            await context.send(f"You have no credits. Please purchase credits to use DALL-E.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))

