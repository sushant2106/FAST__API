# from fastapi import APIRouter,Depends,status,HTTPException,Response
# from sqlalchemy.orm import Session
# from app.database import get_db
# from  .. import models, schemas,utils,oauth2
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm



# router=APIRouter(tags=['Authentication'])

# @router.post('/login')
# def login(user_credential:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):

#     user=db.query(models.User).filter(models.User.email==user_credential.email).first()
     
     
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credential")
    
#     if not utils.verify(user_credential.password,user.password):
#         raise HTTPException(status_code=status.HTTP_401_NOT_FOUND,detail="Invalid Credential")
    
#     #create_token
#     access_token=oauth2.create_access_token(data={"user_id":user.id})

    
#     return {"token":access_token,"token_type":"bearer"}

from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    # return token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
