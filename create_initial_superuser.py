from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, create_engine

from app.models import *
from app.routers.users import create_user

SQLITE_FILE_NAME = "database.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

my_connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_URL, connect_args=my_connect_args)


SQLModel.metadata.create_all(engine)
try:
    with Session(engine) as session:
        create_user(UserCreate(username="admin", password="admin"), session)
except IntegrityError as e:
    print(
        "Couldn't create default admin. It probably already exists. Please delete for production. Error details below:"
    )
    print(e)
