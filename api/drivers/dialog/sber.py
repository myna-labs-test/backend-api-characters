from .base import BaseDialogDriver


class SberDriver(BaseDialogDriver):

    @classmethod
    async def generate_text(cls, input_text: str):
        return 'mock answer'