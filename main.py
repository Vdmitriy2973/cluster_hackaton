from fastapi import FastAPI
from routes.user import auth

app = FastAPI()


app.include_router(auth.router)