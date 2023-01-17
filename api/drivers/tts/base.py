from dataclasses import dataclass
from abc import ABC, abstractmethod
from migrations.database.models import Characters


@dataclass
class BaseTTSDriver(ABC):

    @classmethod
    @abstractmethod
    async def generate_tts(cls, input_text: str) -> bytes:
        pass
