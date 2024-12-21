import tomllib
from pydantic import BaseModel
from pathlib import Path
class Settings(BaseModel):
    host: str
    port:int
    user:str
    password:str
    db_name:str

path_to_file = Path(__file__).parent / "settings.toml"

with open(path_to_file,mode="rb") as f:
    settings = Settings.model_validate(tomllib.load(f)["database"])