import sys
from discord.ext import commands
from discord import app_commands
from . import voucher_service_client as vsc

class Credits(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(description="Check your remaining credits.")
    async def credits(self, context: commands.Context):
        await context.defer()

        credits = vsc.get_credits(context.author.id)

        if credits > 1:
            await context.send(f"You have {credits} credits remaining.")
        elif credits == 1:
            await context.send(f"You have {credits} credit remaining.")
        else:
            await context.send(f"You have no credits. Please purchase credits to use DALL-E.")

    @commands.hybrid_command(description="Redeem your credit voucher.")
    @app_commands.describe(voucher_id="Purchased voucher ID.")
    async def redeem(self, context: commands.Context, voucher_id: str):
        voucher = vsc.get_voucher(voucher_id)

        if not voucher:
            await context.send("Voucher not found. Please confirm that the voucher ID is correct.")
            return

        credits = voucher["credits"]

        if voucher["redeemed"]:
            await context.send(f"Voucher already redeemed. You have {credits} credits remaining.")
        else:
            vsc.redeem_voucher(voucher_id, context.author.id)
            await context.send(f"Successfully redeemed voucher. You have {credits} credits remaining.") 
            

async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))

