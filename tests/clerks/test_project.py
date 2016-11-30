# -*- coding: utf-8 -*-
# pylint: skip-file
# flake8: noqa
"""
    clerks.test_project
    ~~~~~~~~~~~~~~~~~~~

    Runs the unit tests for the project generation.

    :copyright: (c) 2016 by John P. Neumann.
    :license: MIT, see LICENSE for more details.
"""
import os

import pytest
from mock import call, patch, Mock, MagicMock

from markdownclerk.clerks import project


@patch('markdownclerk.clerks.project._create_dir')
@patch('markdownclerk.clerks.project.Environment')
@patch('markdownclerk.clerks.project.FileSystemLoader')
@patch('markdownclerk.clerks.project.yaml')
@patch('markdownclerk.clerks.project.fileutils')
@patch('markdownclerk.clerks.project.io')
def test_generate_project_daily_success(mock_io, mock_fileutils, mock_yaml, mock_filesystem_loader, mock_jinja2_environment, mock_create_dir):
    """Tests that generate project daily succeeds."""
    location = os.path.join('output', 'location')
    template_file = os.path.join('template', 'file.md')
    settings_file = os.path.join('settings', 'file.yml')
    mock_yaml.safe_load.return_value = {'vars': {'foo': 'bar', 'baz': 'qux'}, 'settings': {'weeks': 2, 'days': 2}}
    mock_fileutils.atomic_save = MagicMock()
    mock_create_dir.return_value = 0
    result = project.generate_project_daily(location, template_file, settings_file)
    assert 0 == result
    mock_jinja2_environment.assert_called_with(loader=mock_filesystem_loader.return_value, trim_blocks=True)
    mock_filesystem_loader.assert_called_with('template')
    mock_jinja2_environment.return_value.get_template.assert_called_with('file.md')
    expected_directory_calls = [
        call(os.path.join(location, 'week01', 'day01')),
        call(os.path.join(location, 'week01', 'day02')),
        call(os.path.join(location, 'week02', 'day01')),
        call(os.path.join(location, 'week02', 'day02')),
    ]
    mock_create_dir.assert_has_calls(expected_directory_calls, any_order=True)
    mock_fileutils_enter = mock_fileutils.atomic_save.return_value.__enter__.return_value
    mock_render = mock_jinja2_environment.return_value.get_template.return_value.render.return_value
    mock_fileutils_enter.writelines.assert_called_with(mock_render.encode('utf-8'))


@patch('markdownclerk.clerks.project._create_dir')
@patch('markdownclerk.clerks.project.Environment')
@patch('markdownclerk.clerks.project.FileSystemLoader')
@patch('markdownclerk.clerks.project.yaml')
@patch('markdownclerk.clerks.project.fileutils')
@patch('markdownclerk.clerks.project.io')
def test_generate_project_daily_directory_failure(mock_io, mock_fileutils, mock_yaml, mock_filesystem_loader, mock_jinja2_environment, mock_create_dir):
    """Tests that generate project daily succeeds."""
    location = os.path.join('output', 'location')
    template_file = os.path.join('template', 'file.md')
    settings_file = os.path.join('settings', 'file.yml')
    mock_yaml.safe_load.return_value = {'vars': {'foo': 'bar', 'baz': 'qux'}, 'settings': {'weeks': 2, 'days': 2}}
    mock_fileutils.atomic_save = MagicMock()
    mock_create_dir.return_value = 1
    result = project.generate_project_daily(location, template_file, settings_file)
    assert 1 == result


@patch('markdownclerk.clerks.project._create_dir')
@patch('markdownclerk.clerks.project.Environment')
@patch('markdownclerk.clerks.project.FileSystemLoader')
@patch('markdownclerk.clerks.project.yaml')
@patch('markdownclerk.clerks.project.fileutils')
@patch('markdownclerk.clerks.project.io')
def test_generate_project_daily_atomic_save_failure(mock_io, mock_fileutils, mock_yaml, mock_filesystem_loader, mock_jinja2_environment, mock_create_dir):
    """Tests that generate project daily succeeds."""
    location = os.path.join('output', 'location')
    template_file = os.path.join('template', 'file.md')
    settings_file = os.path.join('settings', 'file.yml')
    mock_yaml.safe_load.return_value = {'vars': {'foo': 'bar', 'baz': 'qux'}, 'settings': {'weeks': 2, 'days': 2}}
    mock_fileutils.atomic_save = MagicMock(side_effect=OSError)
    mock_create_dir.return_value = 0
    result = project.generate_project_daily(location, template_file, settings_file)
    assert 1 == result


@pytest.mark.parametrize('mock_side_effect,expected', [(OSError, 1), (None, 0)])
@patch('markdownclerk.clerks.project.fileutils')
def test_create_dir(mock_fileutils, mock_side_effect, expected):
    """Test create dir return codes."""
    mock_fileutils.mkdir_p.side_effect = mock_side_effect
    assert expected == project._create_dir('/foo/bar/baz')
