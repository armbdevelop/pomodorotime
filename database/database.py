from sqlalchemy import create_engine
from settings import Settings
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://pomodoro:password@localhost:5432/pomodoro?client_encoding=utf8', echo=True)

settings = Settings()

Session = sessionmaker(bind=engine)


def get_db_session() -> Session:
    return Session

