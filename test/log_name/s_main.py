from log import get_logger
from s_sub import some_def

# log_main = get_logger(__name__)
log_main = get_logger()

log_main.info('msg from main file')

some_def()
