from uuid import UUID
from fastapi import APIRouter, Form, Body
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from migrations.database.connection.session import get_session
from api.schemas.characters import Character, CharacterTTS, CharacterText, CharacterTTSOut, CharacterTextOut
from api.services.characters import get_available_characters
from api.utils.formatter import format_models
from api.services.characters import generate_text, generate_tts

character_router = APIRouter(tags=["Character functionality"])


@character_router.get("/characters", response_model=list[Character])
async def get_user(
    session: AsyncSession = Depends(get_session)
) -> list[Character]:
    characters = await get_available_characters(session)
    return format_models(characters, Character)


@character_router.post("/character/text", response_model=CharacterTextOut)
async def get_generated_text(
    character_text: CharacterText = Depends(),
    session: AsyncSession = Depends(get_session)
) -> CharacterTextOut:
    generated_text = await generate_text(character_text, session)
    return CharacterTextOut(text=generated_text)


@character_router.post("/character/tts", response_model=CharacterTTSOut)
async def get_generated_tts(
    character_tts: CharacterTTS = Depends(),
    session: AsyncSession = Depends(get_session)
) -> CharacterTTSOut:
    generated_tts = await generate_tts(character_tts, session)
    return CharacterTTSOut(output=generated_tts)
