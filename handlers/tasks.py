from fastapi import APIRouter
from repository.task import get_task_repository
from database.models import Tasks
from schema.schemas import Task
router = APIRouter(prefix="/tasks", tags=['tasks'])


@router.get("/all")
async def get_tasks():
    return get_task_repository().get_task()


@router.post('/')
async def create_task(data: Task):
    db_task = Tasks(**data.model_dump())
    return get_task_repository().create_task(db_task)

