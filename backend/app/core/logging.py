from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="{time} | {level} | {message}"
)

logger.add(
    "logs/app.log",
    rotation="100 MB",
    retention="30 days",
    level="INFO"
)
