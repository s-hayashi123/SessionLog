from typing import Literal
from pydantic import BaseModel


class GoalCreate(BaseModel):
    goal_type: Literal["数値", "定性"]
    title: str
    target_value: float | None = None
    current_value: float | None = None
    memo: str | None = None


class GoalUpdate(BaseModel):
    goal_type: Literal["数値", "定性"] | None = None
    title: str | None = None
    target_value: float | None = None
    current_value: float | None = None
    memo: str | None = None


class GoalResponse(GoalCreate):
    goal_id: str
