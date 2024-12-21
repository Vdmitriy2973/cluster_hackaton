from pydantic import BaseModel,Field
from uuid import uuid4

class User(BaseModel):
    unique_id: uuid4 = Field(description="Уникальный ID пользователя")
    fio: str = Field(description="ФИО пользователя")
    password: str = Field(description="Пароль")
