from pydantic import BaseModel

class create_user_param(BaseModel):
    username: str
    email: str

class search_user_param(BaseModel):
    email: str