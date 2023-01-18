from dataclasses import dataclass
from abc import ABC, abstractmethod
from api.schemas.characters import Character

@dataclass
class BaseDialogDriver(ABC):
    model_id: str

    @classmethod
    @abstractmethod
    def with_default_settings(cls):
        pass

    @classmethod
    def from_character(cls, character: Character):
        cls.model_id = character.model_id
        return cls.with_default_settings()

    @classmethod
    @abstractmethod
    async def generate_text(cls, input_text: str):
        pass
