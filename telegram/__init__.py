import requests
from telegram.update import Update
from telegram.message import Message
from telegram.chat import Chat


class Bot:
    def __init__(self, token):
        self.token = token
        self.api_url = f'https://api.telegram.org/bot{token}/'

    def get_updates(self):
        method = 'getUpdates'
        resp = requests.get(self.api_url + method)
        if resp.status_code == 200:
            result_json = resp.json()['result']
            updates = []
            for result in result_json:
                # create a new Chat object
                chat = Chat(
                    chat_id=result['message']['chat']['id'],
                    first_name=result['message']['chat']['first_name'],
                    last_name=result['message']['chat'].get('last_name'),
                    username=result['message']['chat'].get('username')
                )
                # create a new Message object
                message = Message(
                    message_id=result['message']['message_id'],
                    chat=chat,
                    text=result['message'].get('text'),
                    photo=result['message'].get('photo'),
                    audio=result['message'].get('audio'),
                    document=result['message'].get('document')
                )
                # create a new Update object
                update = Update(
                    update_id=result['update_id'],
                    message=message
                )
                updates.append(update)
            return updates
        else:
            return []

    def send_message(self, chat_id, text):
        method = 'sendMessage'
        params = {'chat_id': chat_id, 'text': text}
        resp = requests.post(self.api_url + method, params)
        return resp
    
    def send_photo(self, chat_id, photo):
        method = 'sendPhoto'
        params = {'chat_id': chat_id, 'photo': photo}
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_audio(self, chat_id, audio):
        method = 'sendAudio'
        params = {'chat_id': chat_id}
        files = {'audio': audio}
        resp = requests.post(self.api_url + method, params, files=files)
        return resp

    def send_document(self, chat_id, document):
        method = 'sendDocument'
        params = {'chat_id': chat_id}
        files = {'document': document}
        resp = requests.post(self.api_url + method, params, files=files)
        return resp
