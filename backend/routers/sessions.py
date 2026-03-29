from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import APIRouter
from crud import session_crud
from models.session import (
    SessionCreate,
    SessionUpdate,
    SessionResponse,
    SessionDetailCreate,
)


router = APIRouter(
    prefix="/members",
)


@router.get("/{member_id}/sessions", response_model=list[SessionResponse])
def get_member_sessions(member_id: str):
    return session_crud.get_member_sessions(member_id)


@router.post("/{member_id}/sessions")
def create_session_log(member_id: str, data: SessionCreate):
    session_date = datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat()
    session_crud.create_session(
        member_id, session_date, data.model_dump(exclude_none=True)
    )
    return {"member_id": member_id, "session_date": session_date}


@router.post("/{member_id}/sessions/{session_date}/details")
def create_session_detail(member_id: str, session_date: str, data: SessionDetailCreate):
    session_crud.create_session_detail(
        member_id, session_date, data.exercise_id, data.model_dump(exclude_none=True)
    )
    return {"member_id": member_id, "session_date": session_date}


@router.put("/{member_id}/sessions/{session_date}")
def update_session(member_id: str, session_date: str, data: SessionUpdate):
    session_crud.update_session(
        member_id, session_date, data.model_dump(exclude_none=True)
    )
    return {"member_id": member_id, "session_date": session_date}


# @router.get("/{member_id}/graph")
# def get_member_graph(member_id: str, exercise_id: str):
#     return session_crud.get_member_graph(member_id, exercise_id)


# @router.get("/{member_id}/body-stats")
# def get_member_body_stats(member_id: str):
#     return session_crud.get_member_body_stats(member_id)
