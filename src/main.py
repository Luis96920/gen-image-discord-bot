import os
import dotenv

from bot import DalleBot

def main():
    dotenv.load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot = DalleBot()
    bot.run(token)

if __name__ == "__main__":
    main()

