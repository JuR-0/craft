from fastapi import APIRouter
from project.schemas.user import User
router = APIRouter(prefix="/user", tags=["users"])


@router.get("")
async def get_users():
    return User.find_all().to_list()


@router.get("/{user_id}")
async def get_user(user_id: str):
    return User.find_one(User.id == user_id)


@router.post("")
async def create_user(user: User):
    return user.insert()
