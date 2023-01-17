from .base import BaseTTSDriver


class GoogleDriver(BaseTTSDriver):

    @classmethod
    async def generate_tts(cls, input_text: str) -> bytes:
        return bytes()