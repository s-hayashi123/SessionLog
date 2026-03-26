from datetime import date
from typing import Optional
from pydantic import BaseModel


class Session(BaseModel):
    session_id: str
    session_date: date
    duration: Optional[int] = None
    weight: Optional[float] = None
    body_fat: Optional[float] = None
    memo: Optional[str] = None


class SessionDetail(BaseModel):
    exercise_id: str
    exercise_member: str
    session_date: date
    sets: int
    reps: int
    weight: float
    custom_exercise_name: Optional[str] = None
