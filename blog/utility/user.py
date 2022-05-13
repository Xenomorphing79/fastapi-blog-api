from fastapi import HTTPException, status
from blog import models, schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")


def create_user(request: schemas.User, db: Session):
    hashed_pw = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name,
                           email=request.email,
                           password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User does not exist")
    return user
