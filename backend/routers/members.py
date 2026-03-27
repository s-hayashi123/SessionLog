from fastapi import APIRouter
from crud import member_crud, session_crud, goal_crud
from uuid import uuid4


router = APIRouter(
    prefix="/members",
)


@router.get("")
def get_members():
    return member_crud.get_members()


@router.get("/{member_id}")
def get_member(member_id: str):
    return member_crud.get_member(member_id)


@router.post("/")
def create_member(data: dict):
    member_id = str(uuid4())
    member_crud.create_member(member_id, data)
    return {"member_id": member_id}


@router.put("/{member_id}")
def update_member(member_id: str, data: dict):
    member_crud.update_member(member_id, data)
    return {"member_id": member_id}


@router.get("/{member_id}/sessions")
def get_member_sessions(member_id: str):
    return session_crud.get_member_sessions(member_id)


@router.post("/{member_id}/sessions")
def create_session_log(member_id: str, data: dict):
    session_date = data.pop("session_date")
    exercise_id = data.pop("exercise_id")
    session_crud.create_session(member_id, session_date, data)
    session_crud.create_session_detail(member_id, session_date, exercise_id, data)
    return {"member_id": member_id, "session_date": session_date}


@router.get("/{member_id}/goals")
def get_member_goals(member_id: str):
    return goal_crud.get_member_goals(member_id)


@router.post("/{member_id}/goals")
def create_goals(member_id: str, data: dict):
    goal_id = str(uuid4())
    goal_crud.create_goal(member_id, goal_id, data)
    return {"goal_id": goal_id}


@router.put("/{member_id}/goals/{goal_id}")
def update_goals(member_id: str, goal_id: str, data: dict):
    goal_crud.update_goal(member_id, goal_id, data)
    return {"goal_id": goal_id}


@router.get("/{member_id}/graph")
def get_member_graph(member_id: str, exercise_id: str):
    return session_crud.get_member_graph(member_id, exercise_id)


@router.get("/{member_id}/body-stats")
def get_member_body_stats(member_id: str):
    return session_crud.get_member_body_stats(member_id)
