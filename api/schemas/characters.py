from uuid import UUID
from pydantic import BaseModel, Field


class Character(BaseModel):
    id: UUID = Field(..., description='Character UUID')
    name: str = Field(..., description='Character name')

    class Config:
        orm_mode: bool = True


class CharacterText(BaseModel):
    character_id: UUID = Field(..., description='Character UUID')
    text: str = Field(..., description='Character text to respond to')


class CharacterTextOut(BaseModel):
    text: str = Field(..., description='Response text')


class CharacterTTS(BaseModel):
    character_id: UUID = Field(..., description='Character UUID')
    text: str = Field(..., description='Character text to speech')


class CharacterTTSOut(BaseModel):
    output: bytes = Field(..., description='Character TTS output')