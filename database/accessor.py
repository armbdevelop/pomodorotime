from sqlalchemy import create_engine
from settings import settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.db_url, echo=settings.DB_ECHO)


Session = sessionmaker(bind=engine)


def get_db_session() -> Session:
    return Session


