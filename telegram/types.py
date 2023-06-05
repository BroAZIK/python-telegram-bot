class Chat:
    def __init__(self, chat_id, first_name, last_name=None, username=None):
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
    
    def to_dict(self):
        return {
            'chat_id': self.chat_id, 
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'username': self.username
        }


class PhotoSize:
    def __init__(self, file_id, file_unique_id, width, height, file_size=None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
    
    def to_dict(self):
        return {
            'file_id': self.file_id, 
            'width': self.width, 
            'height': self.height, 
            'file_size': self.file_size
        }


class Audio:
    def __init__(self, file_id, file_unique_id, duration):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
    
    def to_dict(self):
        return {
            'file_id': self.file_id, 
            'file_unique_id': self.file_unique_id, 
            'duration': self.duration
        }


class Document:
    def __init__(self, file_id, file_unique_id):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
    
    def to_dict(self):
        return {
            'file_id': self.file_id, 
            'file_unique_id': self.file_unique_id
        }


class Message:
    def __init__(self, message_id, chat: Chat, text=None, photo=None, audio=None, document=None):
        self.message_id = message_id
        self.chat = chat
        self.text = text
        self.photo = photo
        self.audio = audio
        self.document = document
    
    def reply_text(self, text, bot):
        return bot.send_message(self.chat.chat_id, text)
    
    def reply_photo(self, photo, bot):
        return bot.send_photo(self.chat.chat_id, photo)
    
    def reply_audio(self, audio, bot):
        return bot.send_audio(self.chat.chat_id, audio)
    
    def reply_document(self, document, bot):
        return bot.send_document(self.chat.chat_id, document)
    
    def to_dict(self):
        return {
            'message_id': self.message_id, 
            'chat': self.chat.to_dict(), 
            'text': self.text, 
            'photo': self.photo, 
            'audio': self.audio, 
            'document': self.document
        }


class Update:
    def __init__(self, update_id, message: Message):
        self.update_id = update_id
        self.message = message
    
    def to_dict(self):
        return {
            'update_id': self.update_id, 
            'message': self.message.to_dict()
        }