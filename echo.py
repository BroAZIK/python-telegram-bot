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
last_update_id = last_update.update_id

while True:
    # wait 1 second
    time.sleep(1)

    # get now update
    now_update = bot.get_updates()[-1]
    now_update_id = now_update.update_id

    # if now update is not same as last update
    if last_update_id != now_update_id:

        # get chat_id
        chat_id = now_update.message.chat.chat_id
        text    = now_update.message.text
        photo   = now_update.message.photo
        document= now_update.message.document
        audio   = now_update.message.audio

        # check text is not None
        if text is not None:
            print("text: ", text)
            # check text
            if text == "/start":
                text = "Hello, I'm a bot!"
            elif text == "/help":
                text = "I'm a bot, please talk to me!"
            else:
                text = "I don't understand what you mean."

            # send message
            bot.send_message(chat_id, text)
        
        # check photo
        elif photo is not None:
            # get photo
            photo = photo[-1]

            # get photo file_id
            file_id = photo.file_id

            # send photo
            bot.send_photo(chat_id, file_id)

        # check document
        elif document is not None:
            # get document
            document = document

            # get document file_id
            file_id = document.file_id

            # send document
            bot.send_document(chat_id, file_id)

        # check audio
        elif audio is not None:
            # get audio
            audio = audio

            # get audio file_id
            file_id = audio.file_id

            # send audio
            bot.send_audio(chat_id, file_id)

        # update last update
        last_update_id = now_update_id
