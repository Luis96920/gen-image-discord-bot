import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
