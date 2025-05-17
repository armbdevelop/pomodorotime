from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from database import Tasks, Categories
from schema.schemas import TaskShema


class TaskRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_tasks(self):
        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(select(Tasks)).scalars().all()
        return tasks

    def get_task(self, task_id) -> Tasks | None:
        with self.db_session() as session:
            tasks: Tasks = session.execute(select(Tasks).where(Tasks.id == task_id)).scalar_one_or_none()
        return tasks

    def create_task(self, task: TaskShema) -> int:
        task_model = Tasks(name=task.name, pomodoro_count=task.pomodoro_count, category_id=task.category_id)
        with self.db_session() as session:
            session.add(task_model)
            session.commit()
            return task_model.id

    def delete_task(self, task_id) -> None:
        query = delete(Tasks).where(Tasks.id == task_id)
        print(query)
        with self.db_session() as session:
            session.execute(query)
            session.commit()

    def get_task_by_category_name(self, category_name) -> list[Tasks] | None:
        query = select(Tasks).join(Categories, Tasks.id == Categories.id).where(Categories.name == category_name)
        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(query).scalars().all()
        return tasks

    def update_task_name(self, task_id: int, name: str) -> Tasks | None:
        query = update(Tasks).where(Tasks.id == task_id).values(name=name).returning(Tasks.id)
        with self.db_session() as session:
            task_id: int = session.execute(query).scalar_one_or_none()
            session.commit()
            return self.get_task(task_id)
