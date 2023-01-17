from gtts import gTTS
from io import BytesIO
from .base import BaseTTSDriver


class GoogleDriver(BaseTTSDriver):

    @classmethod
    async def generate_tts(cls, input_text: str) -> bytes:
        raw_data = BytesIO()
        tts = gTTS(input_text, lang='ru')
        tts.write_to_fp(raw_data)
        return raw_data.read()
