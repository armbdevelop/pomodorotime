from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, declarative_base, DeclarativeBase, declared_attr

# Base = declarative_base()


class Base(DeclarativeBase):
    id: int
    __name__: str

    __allow__unmapped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class Tasks(Base):

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int] = mapped_column(nullable=False)


class Categories(Base):

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[Optional[str]] = None
    name: Mapped[str]

