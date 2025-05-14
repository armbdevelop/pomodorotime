from fastapi import APIRouter, Depends
from dependencies import get_task_repository
from typing import Annotated, List
from database.models import Tasks
from schema.schemas import Task
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=['tasks'])


@router.get(
    "/all",
    response_model=List[Task],
)
async def get_tasks(task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    return task_repository.get_tasks()


@router.post('/')
async def create_task(data: Task):
    db_task = Tasks(**data.model_dump())
    return get_task_repository().create_task(db_task)

