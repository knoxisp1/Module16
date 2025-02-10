from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Создаем пустой список.
users = []


# Создаем класс  User наследованный от Basemodel
class User(BaseModel):
    # Номер пользователя
    id: int
    # Имя пользователя
    username: str
    # Возраст пользователя
    age: int


app = FastAPI()


@app.get('/users', response_model=List[User])
async def get_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def post_user(username: str, age: int):
    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user_id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int):
    for user in users:
        if user_id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
