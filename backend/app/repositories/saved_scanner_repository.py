from sqlalchemy.orm import Session

from app.models.saved_scanner import SavedScanner


class SavedScannerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, scanner: SavedScanner):
        self.db.add(scanner)
        self.db.commit()
        self.db.refresh(scanner)
        return scanner

    def get(self, scanner_id: int):
        return (
            self.db.query(SavedScanner)
            .filter(SavedScanner.id == scanner_id)
            .first()
        )

    def get_all(self, user_id: int):
        return (
            self.db.query(SavedScanner)
            .filter(SavedScanner.user_id == user_id)
            .order_by(SavedScanner.name)
            .all()
        )

    def delete(self, scanner):
        self.db.delete(scanner)
        self.db.commit()
