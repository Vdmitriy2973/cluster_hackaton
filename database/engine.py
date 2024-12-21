from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_conf import db_settings
from database.models import metadata_obj

engine = create_engine(
    url=db_settings.database_url_psycopg
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def initialize_db():
    Base.metadata.create_all(bind=engine)
    metadata_obj.create_all(engine)