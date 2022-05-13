from os import stat
from fastapi import APIRouter, Depends, HTTPException, status
from blog import database
from blog import schemas, database, models, token
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

router = APIRouter(
    tags= ['Authentication']
)

def pw_verify(password, hashed_pw):
    return pwd_cxt.verify(password, hashed_pw)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User does not exist')
    if not pw_verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}