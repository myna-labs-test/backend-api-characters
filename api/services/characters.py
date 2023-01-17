from uuid import UUID
from migrations.database.models import Characters

from api.exceptions.common import BadRequest, NotFoundException, InternalServerError

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, and_, or_
from sqlalchemy.exc import IntegrityError
from api.schemas.characters import CharacterText, CharacterTTS
from api.drivers.get_driver import get_text_driver, get_tts_driver


async def get_available_characters(session: AsyncSession) -> list[Characters]:
    try:
        query = select(Characters).where(
            Characters.is_active==True
        )
        characters = (await session.execute(query)).scalars().all()
        return characters
    except IntegrityError as e:
        raise InternalServerError(e) from e


async def get_character(character_id: UUID, session: AsyncSession) -> Characters:
    try:
        query = select(Characters).where(
            Characters.id == str(character_id)
        )
        character = (await session.execute(query)).scalars().first()
        if not character:
            raise NotFoundException("Character not found")
        return character
    except IntegrityError as e:
        raise InternalServerError(e) from e


async def generate_text(character_text: CharacterText, session: AsyncSession) -> str:
    character = await get_character(character_text.character_id, session)
    driver = get_text_driver(character)
    return await driver.generate_text(character_text.text)


async def generate_tts(character_tts: CharacterTTS, session: AsyncSession) -> bytes:
    character = await get_character(character_tts.character_id, session)
    driver = get_tts_driver(character)
    return await driver.generate_tts(character_tts.text)
