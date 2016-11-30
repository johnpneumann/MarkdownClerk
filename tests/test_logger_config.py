# -*- coding: utf-8 -*-
# pylint: skip-file
# flake8: noqa
"""
    tests.test_logger_config
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Tests the logger config.

    :copyright: (c) 2016 by John P. Neumann.
    :license: MIT, see LICENSE for more details.
"""
import pytest

from markdownclerk import logger_config


def test_logger_config_not_none():
    """Ensure that the base call gets a valid logger config."""
    cfg = logger_config.get_logging_config()
    assert isinstance(cfg, dict)
