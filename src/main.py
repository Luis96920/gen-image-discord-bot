import os
import dotenv
import logging

from bot import DalleBot

def main():
    logging.getLogger().setLevel(logging.INFO)
    dotenv.load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot = DalleBot()
    bot.run(token)

if __name__ == "__main__":
    main()

