from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config  import settings
import psycopg2
from psycopg2.extras import RealDictCursor

db_url="postgresql://postgres:sushant@localhost:5432/fastapi"


#db_url=f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine=create_engine(db_url)

session=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    with session() as db:
        yield db
