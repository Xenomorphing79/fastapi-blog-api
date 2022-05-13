from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from blog.utility import blog

router = APIRouter(prefix='/blog', tags=['Blogs'])


@router.get('', response_model=List[schemas.Show_Blog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/new', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.Show_Blog)
def show_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show_blog(id, db)
    


@router.delete('/delete/{id}', response_model=schemas.Show_Blog)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_func(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)