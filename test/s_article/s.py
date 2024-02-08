import logging.config

ERROR_LOG_FILENAME = ".tryceratops-errors.log"

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': { # The formatter name, it can be anything that I wish
            'format': '%(asctime)s:%(name)s:%(process)d:%(lineno)d " "%(levelname)s %(message)s',  # What to add in the message
            'datefmt': '%Y-%m-%d %H:%M:%S'  # How to display dates
        },
        'simple': {  # The formatter name
            'format': '%(message)s'
        }
    },
    'handlers': {  # The handler name
        'logfile': {
            'formatter': 'default',  # Refer to the formatter defined above
            'level': 'ERROR',  # FILTER: Only ERROR and CRITICAL logs
            'class': 'logging.handlers.RotatingFileHandler',  # OUTPUT: Which class to use
            'filename': ERROR_LOG_FILENAME,  # Param for class above. Defines filename to use, load it from constant
            'backupCount': 2  # Param for class above. Defines how many log files to keep as it grows
        },
        "verbose_output": {  # The handler name
            "formatter": "default",  # Refer to the formatter defined above
            "level": "DEBUG",  # FILTER: All logs
            "class": "logging.StreamHandler",  # OUTPUT: Which class to use
            "stream": "ext://sys.stdout",  # Param for class above. It means stream to console
        }
    },
    'loggers': {
        'tryceratops': {
            'level': 'INFO',
            'handlers': [
                'verbose_output'
            ]
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': [
            'logfile',
            'verbose_output'
        ]
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

# s = logging.getLogger(f'tryceratops')
s = logging.getLogger(__name__)


s.debug('debug msg')
s.info('info msg')
s.warning('warning msg')
s.error('error msg')
s.critical('critical msg')
