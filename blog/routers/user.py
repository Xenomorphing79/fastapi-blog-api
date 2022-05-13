from fastapi import APIRouter, Depends
from blog import database, schemas, oauth2
from sqlalchemy.orm import Session
from blog.utility import user

router = APIRouter(prefix='/user', tags=['Users'])

get_db = database.get_db


@router.post('/create', response_model=schemas.Show_User)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model=schemas.Show_User)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get_user(id, db)