from telegram import Bot
import os
import requests
import time

# get TOKEN from environment variable
TOKEN = os.environ.get('TOKEN', None)

if TOKEN is None:
    print("Please set TOKEN environment variable.")
    exit(1)

# create bot object
bot = Bot(TOKEN)

# get updates
last_update = bot.get_updates()[-1]

while True:
    # get now update
    now_update = bot.get_updates()[-1]

    # if now update is not same as last update
    if now_update.update_id != last_update.update_id:

        # get chat_id
        chat_id = now_update.message.chat.chat_id
        text    = now_update.message.text

        # check text
        if text == "/start":
            text = "Hello, I'm a bot!"
        elif text == "/help":
            text = "I'm a bot, please talk to me!"
        else:
            text = "I don't understand what you mean."

        # send message
        bot.send_message(chat_id, text)

        # update last update
        last_update = now_update
    
    # wait 1 second
    time.sleep(1)

