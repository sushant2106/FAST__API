from datetime import datetime,timedelta,timezone
from authlib.jose import JoseError,jwt
from fastapi import HTTPException,status



SECRET_KEY='my_secret'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRY_MINUTES=30


def create_access_token(data:dict):
    headers={'alg':ALGORITHM}
    expire=datetime.now(timezone.utc)+timedelta(ACCESS_TOKEN_EXPIRY_MINUTES)
    payload=data.copy()
    payload.update({'exp':expire})
    return jwt.encode(headers,payload,SECRET_KEY).decode('utf-8')


def verify_token(token:str):
    try:
        claims=jwt.decode(token,SECRET_KEY)
        claims.validate()
        username=claims.get('sub')
        
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Token missing subject')
        
        return username
    except JoseError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Couldnt validate credential')



