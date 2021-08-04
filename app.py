from configparser import ConfigParser
from pkg.util import newLogger, getLogLevel

parser = ConfigParser()
parser.read("app.cfg")

name = parser.get("LOGGING", "name")
logname = parser.get("LOGGING", "logname")
loglevel = getLogLevel(parser.get("LOGGING", "level"))
logsize = parser.getint("LOGGING", "size")
backups = parser.getint("LOGGING", "backups")

logger = newLogger(name, logname, loglevel, logsize, backups)

for i in range(1, 100):
    logger.info(i)
