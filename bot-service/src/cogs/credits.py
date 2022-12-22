from discord.ext import commands
from . import voucher_service_client as vsc

class Credits(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(description="Check your remaining credits.")
    async def credits(self, context: commands.Context):
        print(context.author.id)
        vouchers = vsc.get_vouchers(context.author.id)
        print(vouchers)
        credits = vouchers[0]["credits"]
        await context.send(f"You have {credits} credits remaining.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))

