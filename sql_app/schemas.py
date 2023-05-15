from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool

class TodoCreate(BaseModel):
    content: str

class Todo(TodoBase):
    task_id: int
    uid: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    uid: int
    todos: list[Todo] = []

    class Config:
        orm_mode = True