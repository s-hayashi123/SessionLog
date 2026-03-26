from fastapi import APIRouter
from crud import member_crud
from uuid import uuid4


router = APIRouter(
    prefix="/members",
)


@router.get("/")
def get_members():
    return member_crud.get_members()


@router.get("/{member_id}")
def get_member(member_id: str):
    return member_crud.get_member(member_id)


@router.post("/")
def create_member(data: dict):
    member_id = str(uuid4())
    return member_crud.create_member(member_id, data)


@router.put("/{member_id}")
def update_member(member_id: str, data: dict):
    return member_crud.update_member(member_id, data)


@router.get("/{member_id}/sessions")
def get_member_sessions(member_id: str):
    pass


@router.post("/{member_id}/sessions")
def create_session_log(member_id: str):
    pass


@router.get("/{member_id}/goals")
def get_member_goals(member_id: str):
    pass


@router.post("/{member_id}/goals")
def create_goals(member_id: str):
    pass


@router.put("/{member_id}/goals/{goal_id}")
def update_goals(member_id: str):
    pass


@router.get("/{member_id}/graph")
def get_member_graph(member_id: str):
    pass


@router.get("/{member_id}/body-stats")
def get_member_body_stats(member_id: str):
    pass
