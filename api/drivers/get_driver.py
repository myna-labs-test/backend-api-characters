from typing import Type
from .dialog import *
from .tts import *
from migrations.database.models.characters import Characters, CharacterTextDriver, CharacterTTSDriver


def get_text_driver(character: Characters) -> Type[BaseDialogDriver]:
    match character.text_driver:
        case CharacterTextDriver.SBER_GPT:
            return SberDriver.from_character(character)


def get_tts_driver(character: Characters) -> Type[BaseTTSDriver]:
    match character.tts_driver:
        case CharacterTTSDriver.GOOGLE_TTS:
            return GoogleDriver()