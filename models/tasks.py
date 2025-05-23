from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from database import Base 


class Tasks(Base):

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int] = mapped_column(nullable=False)


class Categories(Base):

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[Optional[str]] = None
    name: Mapped[str]
