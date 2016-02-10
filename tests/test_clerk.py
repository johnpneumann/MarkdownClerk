#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Runs unit tests for clerk.

.. module:: test_clerk
    :platform: Linux, MacOS, Windows

.. moduleauthor:: johnpneumann

.. note::
    None
"""
# Built In
import unittest

# Third Party
from mock import patch
from click.testing import CliRunner

# Custom
from markdownclerk import clerk


class ClerkTests(unittest.TestCase):
    """Unit tests."""

    def setUp(self):
        self.runner = CliRunner()
        self.path = 'foo'

    def test_main_success(self):
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(clerk.main, [self.path])
            self.assertEqual(result.exit_code, 0)

    def test_main_no_location(self):
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(clerk.main, [])
            self.assertEqual(result.exit_code, 2)

    @patch('markdownclerk.clerk.os.path.exists')
    @patch('markdownclerk.clerk.fileutils.mkdir_p')
    def test_main_success_missing_dir(self, mock_mkdir, mock_exists):
        with self.runner.isolated_filesystem():
            mock_exists.return_value = False
            self.runner.invoke(clerk.main, [self.path])
            mock_mkdir.assert_any_call(self.path)
            mock_exists.assert_called_with(self.path)

    @patch('markdownclerk.clerk.os.path.exists')
    @patch('markdownclerk.clerk.fileutils.mkdir_p')
    def test_main_success_dir_exists(self, mock_mkdir, mock_exists):
        with self.runner.isolated_filesystem():
            mock_exists.return_value = True
            self.runner.invoke(clerk.main, [self.path])
            mock_exists.assert_called_with(self.path)
