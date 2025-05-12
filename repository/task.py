from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from database import Tasks, get_db_session, Categories


class TaskRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_task(self):
        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(select(Tasks)).scalars().all()
        return tasks

    def get_tasks(self, task_id) -> Tasks | None:
        with self.db_session() as session:
            tasks: Tasks = session.execute(select(Tasks)).where(Tasks.id == task_id).scalar_one_or_none()
        return tasks

    def create_task(self, task: Tasks) -> None:
        with self.db_session() as session:
            session.add(task)
            session.commit()

    def delete_task(self, task_id) -> None:
        with self.db_session() as session:
            session.execute(delete(Tasks).where(Tasks.id == task_id))
            session.commit()

    def get_task_by_category_name(self, category_name) -> list[Tasks] | None :
        query = select(Tasks).join(Categories, Tasks.id == Categories.id).where(Categories.name == category_name)
        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(query).scalars().all()
        return tasks


def get_task_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)