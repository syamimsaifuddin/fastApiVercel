from fastapi import APIRouter
from user_service.function import *
from user_service.param import *


user_router = APIRouter()

@user_router.get("/")
def root():
    return 'Hello Idiots'

@user_router.post("/user/create")
def creating_user(item: create_user_param):
    payload = item.dict()
    data = create_user_orm(**payload)
    return data

@user_router.post("/user/search")
def search_user(item: search_user_param):
    payload = item.dict()
    data = search_user_orm(**payload)
    return data
