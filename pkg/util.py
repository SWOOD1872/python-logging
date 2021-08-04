import logging
from logging.handlers import RotatingFileHandler

def newLogger(name: str, logName: str, logLevel: int, maxSize: int, backups: int) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logLevel)

    handler = RotatingFileHandler(
        logName,
        maxBytes=maxSize,
        backupCount=backups
    )
    formatter = logging.Formatter(fmt=' %(name)s :: %(levelname)s :: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

def getLogLevel(level: str) -> int:
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    return levels.get(level.upper()) or levels.get("DEBUG")
