# -*- coding: utf-8 -*-
"""
    markdownclerk.logger_config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Handles the logging configuration for the module.

    :copyright: (c) 2016 by John P. Neumann.
    :license: MIT, see LICENSE for more details.
"""


def get_logging_config():
    """Creates the logging configuration for us with some standard checking.

    Returns:
        dict: The dictionary configuration of the logger.

    """
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s - %(filename)s'
            },
            'simple': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s'
            },
            'verbose': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s - %(filename)s -> (%(lineno)d)'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
        },
        'loggers': {
            'root': {
                'handlers': ['console'],
                'level': 'INFO'
            },
            'markdownclerk': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO'
            },
        },
    }
    return logging_config
