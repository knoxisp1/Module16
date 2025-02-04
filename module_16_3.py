from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Создаем новый словарь
users = {'1': 'Имя:Example, возраст:18'}
valid_username = Annotated[str, Path(min_length=5, max_length=20, description="Enter username")]
valid_age = Annotated[int, Path(ge=18, le=120, description="Enter age")]
valid_id = Annotated[int, Path(ge=0, le=10000000, description="Enter id", example=2)]


# Возращение словаря.
@app.get('/users')
async def get_users():
    return users


# Добавление в словарь пользователя
@app.post('/user/{username}/{age}')
async def post_user(username: str, age: int):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя:{username},возраст:{age}'
    return f'User {user_id} is registered'


# Обновление данных о пользователе
@app.put('/user/{user_id}/{username}/{age}')
async def update_post(user_id=valid_id, username=valid_username, age=valid_age):
    users[user_id] = f'Имя:{username},возраст:{age}'
    return f'User {user_id}  has been updated'


# Удаление данных
@app.delete('/user/{user_id}')
async def delete_user(user_id=valid_id):
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'
