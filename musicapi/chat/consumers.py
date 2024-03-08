import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'lobby'

        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(self.room_name, {'type': 'chat_message', 'message': message})

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({'type': 'chat', 'message': message}))
