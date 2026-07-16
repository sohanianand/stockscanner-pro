from app.models.latest_indicator import LatestIndicator

SCANNER_FIELDS = {

    "close": LatestIndicator.close,

    "volume": LatestIndicator.volume,

    "rsi": LatestIndicator.rsi,

    "ema20": LatestIndicator.ema20,

    "ema50": LatestIndicator.ema50,

    "sma20": LatestIndicator.sma20,

    "macd": LatestIndicator.macd,

    "macd_signal": LatestIndicator.macd_signal,

    "macd_histogram": LatestIndicator.macd_histogram,

    "bb_upper": LatestIndicator.bb_upper,

    "bb_middle": LatestIndicator.bb_middle,

    "bb_lower": LatestIndicator.bb_lower,

}
