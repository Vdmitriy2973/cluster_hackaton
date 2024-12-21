from sqlalchemy import Column, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

metadata_obj = MetaData()

Base = declarative_base()

user = Table(
    'user',
    metadata_obj,
    Column("id", String,primary_key=True,unique=True),
    Column("fio", String),
    Column("password", String),

)
