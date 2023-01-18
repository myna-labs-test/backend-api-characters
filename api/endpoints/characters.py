from fastapi import APIRouter
from fastapi.param_functions import Depends

from api.schemas.characters import Character, CharacterTTS, CharacterText, CharacterTTSOut, CharacterTextOut
from api.services.characters import generate_text, generate_tts

character_router = APIRouter(tags=["Character functionality"])


@character_router.post("/character/text", response_model=CharacterTextOut)
async def get_generated_text(
        character_text: CharacterText = Depends(),
        character: Character = Depends(),
) -> CharacterTextOut:
    generated_text = await generate_text(character_text, character)
    return CharacterTextOut(text=generated_text)


@character_router.post("/character/tts", response_model=CharacterTTSOut)
async def get_generated_tts(
    character_tts: CharacterTTS = Depends(),
    character: Character = Depends(),
) -> CharacterTTSOut:
    generated_tts = await generate_tts(character_tts, character)
    return CharacterTTSOut(output=generated_tts)
