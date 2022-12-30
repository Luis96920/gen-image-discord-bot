# DALL-E Discord Bot

The DALL-E Discord Bot is an easy way to generate images from within your Discord server.

![dalle-bot-demo](https://user-images.githubusercontent.com/91042401/204699963-12629229-1851-456a-8adc-2894b9cd10af.gif)


## Setup

1. Download Python 3 and Docker.

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd dalle-discord-bot 
   ```
   
4. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

5. Add your [OpenAI API key](https://beta.openai.com/account/api-keys) to the `.env` file.

6. Create an application and bot through the [Discord developer portal](https://discord.com/developers/docs/intro). 

7. Create a client secret (i.e. API key) and add to the `.env` file. 

8. Add the following redirect URL in the OAuth2 settings: `https://discordapp.com/oauth2/authorize?&client_id=<client_id>&scope=bot&permissions=274877910016`. The permissions integer allows your bot to read messages, send messages, and send messages in threads. Nothing more.

9. Create an admin guild to invite your bot to. This is where you can test and deploy new commands using the sync command. Note that *guild* is the terminology used throughout the developer documentation, whereas *server* is the user-facing terminology.

10. Add the admin guild ID to the `.env` file. You can find this ID by opening Discord in a browser and checking the URL: `https://discord.com/channels/**<guild_id>**/<channel_id>`

11. Build bot-service and voucher-service images:

      ```bash
      $ cd bot-service 
      $ docker build . -t <name>
      $ cd ../voucher-service
      $ docker build . -t <name> 
      ```

12. Run the application via docker compose

      ```bash
      $ docker compose up
      ```

12. Create and redeem credit vouchers via the create (hidden; ! prefix only) and redeem commands. *(Feel free to tear out the voucher service in your fork. I only created it to play around with Flask, Docker networking, and EBS volumes.)*

13. Add your bot to any Discord guild. Generate an image with the /generate command.


## Dockerless Setup

Follow all of the above, except you can replace step 11 with:

1. In bot-service, create a new virtual environment:

   ```bash
   $ python3 -m venv venv
   $ . venv/bin/activate
   ```

2. Install the requirements:

   ```bash
   $ pip3 install -r requirements.txt
   ```
   
3. Run the app:

   ```bash
   $ python3 main.py
   ```

4. Repeat 1-3 for voucher-service.

