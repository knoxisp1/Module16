from fastapi import Path, FastAPI
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_id_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]) -> dict:
    return {"message": f"Вы вошли  как пользователь № {user_id}"}


@app.get("/user")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username")],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age")]):
    return {"message": f"Информация о пользователе.Имя:{username},Возраст:{age}"}
