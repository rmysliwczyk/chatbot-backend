from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.dependencies import create_db_and_tables
from app.routers import auth, users


@asynccontextmanager
async def my_lifespan(app: FastAPI):
    # Startup
    create_db_and_tables()
    yield
    # Shutdown


app = FastAPI(lifespan=my_lifespan)

app.include_router(auth.router)
app.include_router(users.router)
