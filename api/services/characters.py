from api.schemas.characters import CharacterText, CharacterTTS, Character
from api.drivers.get_driver import get_text_driver, get_tts_driver


async def generate_text(character_text: CharacterText, character: Character) -> str:
    driver = get_text_driver(character)
    return await driver.generate_text(character_text.text)


async def generate_tts(character_tts: CharacterTTS, character: Character) -> bytes:
    driver = get_tts_driver(character)
    return await driver.generate_tts(character_tts.text)
