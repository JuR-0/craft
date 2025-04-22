from fastapi import APIRouter
from craft.schemas.user import DbUser, User
from craft.auth.password import hash_password

router = APIRouter(prefix="/user", tags=["users"])


@router.get("")
async def get_users():
    return DbUser.find_all().to_list()


@router.get("/{user_id}")
async def get_user(user_id: str):
    return DbUser.find_one(DbUser.id == user_id)


@router.post("")
async def create_user(user: User):
    return DbUser(**user).insert()
