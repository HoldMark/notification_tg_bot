import sys
import logging
from logging import StreamHandler, Formatter
from logging.handlers import RotatingFileHandler
from src.core.config import LOGS_DIR

LOGS_PATH_LIBS = f'{LOGS_DIR}/libs'
LOGS_PATH_PROJECT = f'{LOGS_DIR}/project'


def namer(name):
    return name + '.log'


default_formatter = Formatter(
    fmt='%(filename)s:%(lineno)d #%(levelname)s [%(asctime)s] - %(name)s - %(message)s'
)

sh = StreamHandler(stream=sys.stdout)
sh.setFormatter(default_formatter)

rfh_libs = RotatingFileHandler(filename=f'{LOGS_PATH_LIBS}.log', mode='a', maxBytes=200_000_000, backupCount=2)
rfh_libs.setFormatter(default_formatter)
rfh_libs.namer = namer

rfh_project = RotatingFileHandler(filename=f'{LOGS_PATH_PROJECT}.log', mode='a', maxBytes=200_000_000, backupCount=2)
rfh_project.setFormatter(default_formatter)
rfh_project.namer = namer


root_logger = logging.getLogger()
root_logger.setLevel('INFO')

root_logger.addHandler(sh)
root_logger.addHandler(rfh_libs)

bot_logger = logging.getLogger('bot')
bot_logger.setLevel('DEBUG')

bot_logger.addHandler(sh)
bot_logger.addHandler(rfh_project)

bot_logger.propagate = False
