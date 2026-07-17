from app.models.saved_scanner import SavedScanner
from app.repositories.saved_scanner_repository import SavedScannerRepository


class SavedScannerService:

    def __init__(self, db):
        self.repo = SavedScannerRepository(db)

    def create(self, user_id: int, request):

        scanner = SavedScanner(
            user_id=user_id,
            name=request.name,
            description=request.description,
            definition=request.definition,
        )

        return self.repo.create(scanner)

    def list(self, user_id: int):
        return self.repo.get_all(user_id)

    def delete(self, scanner_id: int):

        scanner = self.repo.get(scanner_id)

        if scanner is None:
            return None

        self.repo.delete(scanner)

        return True
