from fastapi import APIRouter, Depends
from starlette import status

from dependencies import get_task_repository
from typing import Annotated, List
from database.models import Tasks
from schema.schemas import TaskShema
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=['tasks'])


@router.get(
    "/all",
    response_model=List[TaskShema],
)
async def get_tasks(task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    return task_repository.get_tasks()


@router.post(
    '/',
    response_model=TaskShema,
)
async def create_task(
        task: TaskShema,
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)]
):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task


@router.patch(
    '/{task_id}',
    response_model=TaskShema,
)
async def patch_task(
        task_id: int,
        name: str,
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)]
):
    return task_repository.update_task_name(task_id, name)


@router.delete(
    '/delete/{task_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(
        task_id: int,
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)]
):
    task_repository.delete_task(task_id)
    return {'message': "task deleted"}
