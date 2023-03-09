import logging

from rich.logging import RichHandler


def get_logger(level=logging.INFO, name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(RichHandler())
    return logger
