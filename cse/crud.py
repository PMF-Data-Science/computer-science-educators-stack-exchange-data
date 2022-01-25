### crud.py ###

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL
from models import Base

engine = create_engine(DATABASE_URL)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
