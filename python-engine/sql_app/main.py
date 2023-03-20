import json
import uuid
import hashlib

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Login Sessions store in runtime. No Redis :(
user_sessions = {}

""" # Example:
{ 
    "10": {
      "token": "8595bdaa-c2a2-4b4e-98b3-002053b95408"
    },
    "11": {
      "token": "8abecd65-bcb5-4f28-9b14-85f249acf4ed"
}
"""

@app.post("/user/register", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    result = crud.create_user(db=db, user=user)
    # Optionally try to catch 400, but better 422
    return result


@app.post("/user/login", response_model=None)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.id)

    if db_user.hashed_password == hashlib.sha1(user.password.encode()).hexdigest():
        login_attributes = {'token': uuid.uuid4()}
        user_sessions[db_user.id] = login_attributes
        return login_attributes #, user_sessions
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    raise HTTPException(status_code=400, detail="Невалидные данные")


#@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/get/{id}", response_model=schemas.User)
def read_user(id: int, db: Session = Depends(get_db)):
    #400, но 422 parser срабатывает раньше
    db_user = crud.get_user(db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Анкета не найдена")
    return db_user

