from custom.channels.AsyncJsonWebsocketConsumer import CustomAsyncJsonWebsocketConsumer


class ChatJsonConsumer(CustomAsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = "socket"
        super().__init__(*args, **kwargs)

    async def connect(self):
        await self.post_connect()
        # Connect to group
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "chat_message",
                "text": text_data if text_data else bytes_data.decode("utf-8"),
            },
        )

    async def chat_message(self, event):
        data = await self.decode_json(event["text"])
        await self.send_json({"dj": str(self.user)})

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        await self.close(code)
