from fastapi import APIRouter,Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from blog import schemas,database,models,token
from blog.hashing import Hash
from sqlalchemy.orm import Session


router = APIRouter(tags=["Authentication"])

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog import models, schemas, database, token
from blog.hashing import Hash

router = APIRouter(tags=["login"])


@router.post("/login", response_model=schemas.Token)
def login(
    request: OAuth2PasswordRequestForm = Depends(),  # use Depends here for form parsing
    db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

