from pydantic import BaseModel, Field, model_validator


class TaskShema(BaseModel):
    id: int | None = None
    name: str
    pomodoro_count: int
    category_id: int

    @model_validator(mode='after')
    def check_name_or_pc_is_not_none(self):
        if self.name is None or self.pomodoro_count is None:
            raise ValueError("")
        return self
