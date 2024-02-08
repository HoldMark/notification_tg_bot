from log import get_logger

log_def = get_logger()


def some_def():
    log_def.info('msg from sub file')
    pass
