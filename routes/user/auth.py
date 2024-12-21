from fastapi import  APIRouter,Depends
from configuration.config import settings
from pydantic import BaseModel, Field
import uuid
from sqlalchemy import insert
from sqlalchemy.orm import Session
from database.engine import SessionLocal
from database.models import user as user_table
router = APIRouter(prefix="/auth",tags=["/auth"])


class User(BaseModel):
    fio: str = Field(None)
    password: str = Field(None)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def sign_in(user: User,db: Session = Depends(get_db)):
    db.execute(insert(user_table).values(
        id=uuid.uuid4(),
        fio=user.fio,
        password=user.password)
    )
    db.commit()
    return {"status":"success"}