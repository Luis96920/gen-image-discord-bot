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
        person_id = context.author.id
        vsc.redeem_voucher(voucher_id, person_id)
        credits = vsc.get_credits(person_id)
        context.send(f"Successfully redeemed voucher. You have {credits} credits remaining.") 
            
async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))

