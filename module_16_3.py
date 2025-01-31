from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя:Example,возраст:18'}

valid_username = Annotated[str, Path(min_length=5, max_length=20, description="Enter username")]
valid_age = Annotated[int, Path(ge=18, le=120, description="Enter age")]
valid_id = Annotated[int, Path(ge=0, le=10000000, description="Enter id", example=2)]


@app.get("/")
async def Get_Users():
    return users


@app.post("/user/{username}/{age}")
async def Post_User(username: valid_username, age: valid_age) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def Update_User(user_id=valid_id, username=valid_username, age=valid_age) -> str:
    users[user_id] = f"Имя:{username},возраст {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def Delete_User(user_id=valid_id) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"
