from pydantic import BaseModel


class Exercise(BaseModel):
    exercise_id: str
    name: str
    muscle_group: str
