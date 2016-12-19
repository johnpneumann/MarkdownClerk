# -*- coding: utf-8 -*-
"""
    markdownclerk
    ~~~~~~~~~~~~~
    A simple markdown project tracking generator.

    :copyright: (c) 2016 by John P. Neumann.
    :license: MIT, see LICENSE for more details.
"""
from __future__ import absolute_import

import logging
import logging.config

from . import logger_config


__version__ = '0.2.2'
LOGGING_CONFIG = logger_config.get_logging_config()
logging.config.dictConfig(LOGGING_CONFIG)
