import sys

from loguru import logger

logger.remove()
logger.add(sys.stdout, enqueue=True, catch=True)
