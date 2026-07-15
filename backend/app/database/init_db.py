from app.database.database import engine
from app.database.base import Base


def init_database():
    Base.metadata.create_all(bind=engine)
