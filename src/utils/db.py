from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from src.utils.settings import settings

Base = declarative_base()

Engine = create_engine(url =settings.DB_CONNECTION)

Localsession = sessionmaker(bind = Engine)


def get_db():
    session =Localsession()
    try:
        yield session
    finally:
        session.close()