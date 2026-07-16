from typing import Generic
from typing import Type
from typing import TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(
        self,
        model: Type[T],
        db: Session,
    ):
        self.model = model
        self.db = db

    def get(self, id: int):

        return (
            self.db.query(self.model)
            .filter(self.model.id == id)
            .first()
        )

    def get_all(self):

        return self.db.query(self.model).all()

    def create(self, obj):

        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj

    def update(self):

        self.db.commit()

    def delete(self, obj):

        self.db.delete(obj)

        self.db.commit()
