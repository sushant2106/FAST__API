from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="postgresql://postgres:sushant@localhost/fastapi"

engine=create_engine(db_url)

session=sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db():
    with session() as db:
        yield db
