from fastapi import APIRouter


router = APIRouter(
    prefix="/members",
)


@router.get("/")
def get_members():
    pass


@router.get("/{member_id}")
def get_member():
    pass


@router.post("/")
def create_member():
    pass


@router.put("/{member_id}")
def update_member():
    pass


@router.get("/{member_id}/sessions")
def get_member_sessions():
    pass


@router.post("/{member_id}/sessions")
def create_session_log():
    pass


@router.get("/{member_id}/goals")
def get_member_goals():
    pass


@router.post("/{member_id}/goals")
def create_goals():
    pass


@router.put("/{member_id}/goals/{goal_id}")
def update_goals():
    pass


@router.get("/{member_id}/graph")
def get_member_graph():
    pass


@router.get("/{member_id}/body-stats")
def get_member_body_stats():
    pass
