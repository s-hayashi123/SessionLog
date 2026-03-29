from datetime import date
from pydantic import BaseModel


class SessionCreate(BaseModel):
    duration: int | None = None
    weight: float | None = None
    body_fat: float | None = None
    memo: str | None = None


class SessionDetailCreate(BaseModel):
    exercise_id: str
    sets: int
    reps: int
    weight: float
    custom_exercise_name: str | None = None


class SessionUpdate(BaseModel):
    duration: int | None = None
    weight: float | None = None
    body_fat: float | None = None
    memo: str | None = None


class SessionResponse(BaseModel):
    session_date: date
    duration: int | None = None
    weight: float | None = None
    body_fat: float | None = None
    memo: str | None = None


class SessionDetailResponse(BaseModel):
    exercise_id: str
    sets: int
    reps: int
    weight: float
    custom_exercise_name: str | None = None
