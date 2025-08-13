from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from blog.hashing import Hash
from blog.repository import user

from .. import schemas, models
from ..database import get_db
    

router = APIRouter(
    prefix="/user",
    tags=["Users"])


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)
    

@router.get("/",response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)
    




