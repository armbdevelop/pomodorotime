from sqlalchemy import create_engine
from settings import Settings
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pomodoro.sqlite', echo=True)

settings = Settings()

Session = sessionmaker(bind=engine)


def get_db_session() -> Session:
    return Session

