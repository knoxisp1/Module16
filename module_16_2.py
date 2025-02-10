from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def main_page():
    return "Главная страница"


@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как Администратор"


@app.get("/user/{user_id}")
async def get_user_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username")],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter Age")]):
    return f"Информация о пользователе. Имя:{username},Возраст:{age}"
