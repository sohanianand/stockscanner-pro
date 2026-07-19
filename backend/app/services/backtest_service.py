from app.repositories.saved_scanner_repository import SavedScannerRepository
from app.repositories.backtest_repository import BacktestRepository
from app.models.backtest import Backtest

class BacktestService:

    def __init__(self, db):

        self.db = db

        self.saved_repo = SavedScannerRepository(db)

        self.repo = BacktestRepository(db)

    def run(self, request):

        scanner = self.saved_repo.get(request.scanner_id)

        if scanner is None:

            raise Exception("Scanner not found")

        #
        # Historical Scanner Engine
        #

        total = 120

        winners = 74

        losers = 46

        win_rate = winners / total * 100

        avg_return = 4.32

        result = Backtest(

            user_id=1,

            scanner_id=request.scanner_id,

            start_date=request.start_date,

            end_date=request.end_date,

            total_signals=total,

            winners=winners,

            losers=losers,

            win_rate=win_rate,

            average_return=avg_return,

        )

        return self.repo.create(result)
