from fastapi import FastAPI
from user_service.api import user_router
from swagger import swagger_router

app = FastAPI()

app.include_router(user_router, prefix="")
app.include_router(swagger_router, prefix="")