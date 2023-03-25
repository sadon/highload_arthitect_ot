from sqlalchemy.orm import Session

from . import models, schemas

import hashlib


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_users_by_fl_names(db: Session, first_prefix = "", second_prefix = "", skip: int = 0, limit: int = 100):

    query =  db.query(models.User).filter(
        models.User.first_name.like(f"{first_prefix}%"),
        models.User.second_name.like(f"{second_prefix}%")
    ).offset(skip).limit(limit)#.all()

    print(query)
    return query.all()


def create_user(db: Session, user: schemas.UserCreate):
    to_db_user = user.dict()
    to_db_user['hashed_password'] = hashlib.sha1( user.password.encode()).hexdigest()
    del to_db_user['password']
    db_user = models.User(**to_db_user)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


"""
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
"""