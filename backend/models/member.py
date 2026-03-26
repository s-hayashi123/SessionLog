from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel


class Member(BaseModel):
    name: str
    age: int
    gender: Literal["男性", "女性", "その他"]
    height: float
    weight: float
    body_fat: float
    joined_at: datetime
    memo: Optional[str] = None
