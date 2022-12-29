import sys
from discord.ext import commands
from discord import app_commands
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

    @commands.hybrid_command(description="Redeem your credit voucher.")
    @app_commands.describe(voucher_id="Purchased voucher ID.")
    async def redeem(self, context: commands.Context, voucher_id: str):
        voucher = vsc.get_voucher(voucher_id)
        
        if not voucher:
            await context.send("Voucher not found. Please confirm that the voucher ID is correct.")
            return

        if voucher["redeemed"]:
            credits = vsc.get_credits(context.author.id)
            creditsString = "credit" if credits == 1 else "credits"
            await context.send(f"Voucher already redeemed. You have {credits} {creditsString} remaining.")
        else:
            vsc.redeem_voucher(voucher_id, context.author.id)
            credits = vsc.get_credits(context.author.id)
            creditsString = "credit" if credits == 1 else "credits"
            await context.send(f"Successfully redeemed voucher. You have {credits} {creditsString} remaining.") 
            
    @commands.command(hidden=True)
    @commands.is_owner()
    @commands.guild_only()
    async def create(self, context: commands.Context, credits: str):
        voucher = vsc.create_voucher(credits)
        voucher_id = voucher["voucher_id"]
        await context.send(f"Successfully created voucher: {voucher_id}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))

