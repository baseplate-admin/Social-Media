from channels.generic.websocket import AsyncJsonWebsocketConsumer


class CustomAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def post_connect(self):
        """
        Maps the following attributes:
            user -> self.user
        """
        self.user = self.scope["user"]

    # @classmethod
    # async def decode_json(cls, text_data) -> dict:
    #     return orjson.loads(text_data)

    # @classmethod
    # async def encode_json(cls, content) -> dict:
    #     # Orjson uses binary format. Decode it
    #     return orjson.dumps(content).decode("utf-8")
