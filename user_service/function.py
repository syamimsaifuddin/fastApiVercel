from user_service.model import *
import json

def testing():
    return 'Hello'

def create_user(**param):

    js = json.load(open(r"C:\Users\syami\OneDrive\Desktop\fastApi\backend\user_db.json", "r"))

    name_to_check = param['name']
    exist = any(obj['name'] == name_to_check for obj in js)

    if exist:
        return f"Failed to create use {param['name']} since its already in db"
    else:

        js.append(param)

        json.dump(js, open(r"C:\Users\syami\OneDrive\Desktop\fastApi\backend\user_db.json", "w"))

        return f"User {param['name']} successfully created"
    
def create_user_orm(**param):

    check_if_exist = search(User, **param)
    
    if check_if_exist:
        return 'User already exist'
    else:
        response = insert(User, **param)
        return response
    
def search_user_orm(**param):

    find_user = search(User, **param)

    if find_user:
        return find_user
    else:
        return 'User does not exist'