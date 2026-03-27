from typing import Literal, Optional
from pydantic import BaseModel


class Goal(BaseModel):
    goal_id: str
    goal_type: Literal["数値", "定性"]
    title: str
    target_value: Optional[float] = None
    current_value: Optional[float] = None
    memo: Optional[str] = None
