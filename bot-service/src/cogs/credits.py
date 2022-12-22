from discord.ext import commands

class Credits(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(description="Check your remaining credits.")
    async def credits(self, context: commands.Context):
        await context.send("You have 7 credits remaining.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))

