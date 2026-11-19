from fastapi import FastAPI

from fast_api_crud_de_usuario.src.main.routes.users_routes import users_routes

app = FastAPI()
app.include_router(users_routes)
