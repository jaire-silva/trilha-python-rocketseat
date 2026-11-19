from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["users"])


@users_routes.post("/users")
async def create_user():
    return JSONResponse(
        content={
            "message": "User created"
        },
        status_code=201
    )
