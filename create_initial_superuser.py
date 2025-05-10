import os

from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, create_engine

from app.models import *
from app.routers.users import create_user

load_dotenv()

DEFAULT_ADMIN_LOGIN = os.getenv("DEFAULT_ADMIN_LOGIN")
DEFAULT_ADMIN_PASSWORD = os.getenv("DEFAULT_ADMIN_PASSWORD")

SQLITE_FILE_NAME = "database.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

my_connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_URL, connect_args=my_connect_args)


SQLModel.metadata.create_all(engine)
try:
    with Session(engine) as session:
        create_user(
            UserCreate(username=DEFAULT_ADMIN_LOGIN, password=DEFAULT_ADMIN_PASSWORD),
            session,
        )
except IntegrityError as e:
    print("Couldn't create default admin. Error details below:")
    print(e)
