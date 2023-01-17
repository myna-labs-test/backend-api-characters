from dataclasses import dataclass
from abc import ABC, abstractmethod
from migrations.database.models import Characters


@dataclass
class BaseDialogDriver(ABC):
    model_id: str

    @classmethod
    def from_character(cls, character: Characters):
        return cls(model_id=character.model_id)

    @classmethod
    @abstractmethod
    async def generate_text(cls, input_text: str):
        pass
