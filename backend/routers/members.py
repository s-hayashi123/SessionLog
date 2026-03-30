from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import APIRouter, HTTPException
from crud import member_crud
from uuid import uuid4
from models.member import MemberCreate, MemberResponse, MemberUpdate


router = APIRouter(
    prefix="/members",
)


@router.get("", response_model=list[MemberResponse])
def get_members():
    return member_crud.get_members()


@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: str):
    member = member_crud.get_member(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@router.post("")
def create_member(data: MemberCreate):
    member_id = str(uuid4())
    item = data.model_dump(exclude_none=True)
    item["joined_at"] = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat()
    member_crud.create_member(member_id, item)
    return {"member_id": member_id}


@router.put("/{member_id}")
def update_member(member_id: str, data: MemberUpdate):
    member_crud.update_member(member_id, data.model_dump(exclude_none=True))
    return {"member_id": member_id}
