from passlib.context import CryptContext

pwd_context=CryptContext(schemes=['bcrypt'],deprecatd='auto')

fake_user={
    'johndoe':{
        'username':'johndoe',
        'hashed_password':pwd_context.hash('secret123')
    }
}


def get_user(username:str):
    user=fake_user.get(username)
    return user


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

