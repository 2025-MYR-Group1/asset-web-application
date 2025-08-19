from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

from app.core.settings import Settings

settings = Settings()
postgres_url = settings.db_url
engine = create_engine(postgres_url)


def create_db_and_tables():
    """
    Create all tables in the database
    """

    SQLModel.metadata.create_all(engine)


def get_session():
    """
    Get a session from the database
    """

    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
