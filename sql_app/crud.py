from sqlalchemy.orm import Session
from sqlalchemy import delete
import models, schemas

#user methods 
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#method for creating new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email, auth=user.auth)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#method for deleting user
def delete_user(db: Session, user_id: int):
    db_user = db.get(models.User, user_id)
    db.delete(db_user)
    db.commit()
    return db_user

#task methods
#method for getting all tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

#method for creating specific user's task
def create_usertask(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_todo = models.Todo(**todo.dict(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

