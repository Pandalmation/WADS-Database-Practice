from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    auth_provider = Column(String, index= True)

    todos = relationship("Todo", back_populates="owner")

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key= True, index = True)
    title = Column(String, index= True)
    description = Column(String, index=True)
    completed = Column(Boolean, default= False)
    uid = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="todos")