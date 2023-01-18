from typing import Type
from .dialog import *
from .tts import *
from api.schemas.characters import Character


def get_text_driver(character: Character) -> Type[BaseDialogDriver]:
    match character.text_driver:
        case "SBER_GPT":
            return SberDriver.from_character(character)


def get_tts_driver(character: Character) -> Type[BaseTTSDriver]:
    match character.tts_driver:
        case "GOOGLE_TTS":
            return GoogleDriver()