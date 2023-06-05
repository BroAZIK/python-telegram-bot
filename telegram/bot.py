import requests
from telegram.types import Update, Message, Chat, Audio, Document, PhotoSize

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
                # check if photo is available
                if result['message'].get('photo'):
                    photo = []
                    for p in result['message']['photo']:
                        photo.append(PhotoSize(
                            file_id=p['file_id'],
                            file_unique_id=p['file_unique_id'],
                            width=p['width'],
                            height=p['height']
                        ))
                else:
                    photo = None
                
                # check if audio is available
                if result['message'].get('audio'):
                    audio = Audio(
                        file_id=result['message']['audio']['file_id'],
                        file_unique_id=result['message']['audio']['file_unique_id'],
                        duration=result['message']['audio']['duration']
                    )
                else:
                    audio = None
                
                # check if document is available
                if result['message'].get('document'):
                    document = Document(
                        file_id=result['message']['document']['file_id'],
                        file_unique_id=result['message']['document']['file_unique_id']
                    )
                else:
                    document = None

                # create a new Chat object
                chat = Chat(
                    chat_id=result['message']['chat']['id'],
                    first_name=result['message']['chat'].get('first_name'),
                    last_name=result['message']['chat'].get('last_name'),
                    username=result['message']['chat'].get('username')
                )

                # create a new Message object
                message = Message(
                    message_id=result['message']['message_id'],
                    chat=chat,
                    text=result['message'].get('text'),
                    photo=photo,
                    audio=audio,
                    document=document
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
        params = {'chat_id': chat_id, 'audio': audio}
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_document(self, chat_id, document):
        method = 'sendDocument'
        params = {'chat_id': chat_id, 'document': document}
        resp = requests.post(self.api_url + method, params)
        return resp
