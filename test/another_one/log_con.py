import logging.config

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s:%(name)s:%(process)d:%(lineno)d " "%(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "stdout": {
            "formatter": "default",
            "level": "DEBUG",
            "class": "logging.StreamHandler",  # OUTPUT: Which class to use
            "stream": "ext://sys.stdout"  # Param for class above. It means stream to console
        }
    }
}

logging.config.dictConfig(LOGGING)
