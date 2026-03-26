from fastapi import APIRouter


router = APIRouter(
    prefix="/trainers",
)


@router.get("/")
def get_trainers():
    pass
