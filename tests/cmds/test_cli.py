# -*- coding: utf-8 -*-
# pylint: skip-file
# flake8: noqa
"""
    cmds.test_cli
    ~~~~~~~~~~~~~

    Runs the unit tests for the CLI.

    :copyright: (c) 2016 by John P. Neumann.
    :license: MIT, see LICENSE for more details.
"""
import os

import pytest
from mock import patch
from click import testing, UsageError

from markdownclerk.cmds import cli


@pytest.fixture
def clirunner():
    """CLI runner fixture."""
    return testing.CliRunner()


def test_cli_version(clirunner):
    """Ensure that the cli version is called correctly."""
    result = clirunner.invoke(cli.markdownclerk, ['--version'])
    assert result.exception is None
    assert 0 == result.exit_code


@pytest.mark.parametrize('mock_project_return_value,expected', [(0, 0), (1, 2)])
@patch('markdownclerk.cmds.cli.project')
def test_time_based_project(mock_project, mock_project_return_value, expected, clirunner):
    """Test that the cli runner exits with the appropriate exit code."""
    mock_project.generate_project_daily.return_value = mock_project_return_value
    with clirunner.isolated_filesystem():
        pth = os.getcwd()
        template_path = os.path.join(pth, 'template')
        location = os.path.join(pth, 'output_location')
        template_file = os.path.join(template_path, 'template.md')
        config_file = os.path.join(template_path, 'config.yml')
        os.makedirs(template_path)
        os.makedirs(location)
        with open(template_file, 'w') as fopen:
            fopen.write('template')
        with open(config_file, 'w') as fopen:
            fopen.write('config')
        result = clirunner.invoke(cli.time_based_project, [pth, '--template-file', template_file,
                                                           '--config-file', config_file])
        assert expected == result.exit_code
