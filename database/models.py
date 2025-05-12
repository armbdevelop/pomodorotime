from sqlalchemy.orm import  Mapped, mapped_column, declarative_base

Base = declarative_base()


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

