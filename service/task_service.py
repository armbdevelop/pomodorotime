from dataclasses import dataclass
from repository import TaskRepository, TaskCache
from schema.schemas import TaskShema


@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache

    def get_tasks(self) -> list[TaskShema]:
        if tasks := self.task_cache.get_tasks():
            return tasks

        tasks = self.task_repository.get_tasks()
        tasks_schema = [TaskShema.model_validate(task) for task in tasks]
        self.task_cache.set_task(tasks_schema)
        return tasks
