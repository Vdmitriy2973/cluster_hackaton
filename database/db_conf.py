import dataclasses
from configuration.config import settings

@dataclasses.dataclass
class DataBaseSettings:
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def database_url_psycopg(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


db_settings = DataBaseSettings(settings.host, settings.port, settings.user, settings.password, settings.db_name)