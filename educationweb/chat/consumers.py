import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import *
class ChatConsumer(WebsocketConsumer):

    
    def fetch_messages(self, data):
        chat=Chat.objects.filter(id=int(data['chatId'])).first()
        messages = chat.messages.all() #############
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        current_chat=Chat.objects.filter(id=data['chatId']).first()
        user_contact = User.objects.filter(username=data['sender']).first()
        message = Message.objects.create(
            chat=current_chat,
            sender=user_contact,
            message=data['message'],
            )
        current_chat.messages.add(message)
        current_chat.save()
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': message.id,
            'sender': message.sender.username,
            'message': message.message,
            'date': str(message.date),
            'sender_type':message.sender_type
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }





    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                
            }
        )

    # Receive message from room group
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data
        if data["sender"] != self.scope["user"].username :
            print(self.scope["user"],data["sender"])
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        
        self.send(text_data=json.dumps(message))
