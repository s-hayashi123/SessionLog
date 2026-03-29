from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class MemberCreate(BaseModel):
    name: str
    age: int
    gender: Literal["男性", "女性", "その他"]
    height: float
    weight: float
    body_fat: float
    memo: str | None = None


class MemberUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    gender: Literal["男性", "女性", "その他"] | None = None
    height: float | None = None
    weight: float | None = None
    body_fat: float | None = None
    joined_at: datetime | None = None
    memo: str | None = None


class MemberResponse(BaseModel):
    member_id: str
    name: str
    age: int
    gender: Literal["男性", "女性", "その他"]
    height: float
    weight: float
    body_fat: float
    joined_at: datetime
    memo: str | None = None
