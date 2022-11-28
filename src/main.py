import asyncio
import dotenv
import os

from bot import DalleBot

def main():
    dotenv.load_dotenv()
    bot = DalleBot()
    bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    main()

