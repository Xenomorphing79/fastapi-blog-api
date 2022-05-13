from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from blog import models, schemas, database
from http import HTTPStatus


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog does not exist")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

def update_blog(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog does not exist")
    blog.update(request.dict())
    db.commit()
    return 'Updated'

def show_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog does not exist")
    return blog