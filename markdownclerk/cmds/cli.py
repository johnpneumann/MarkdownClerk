# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""
    cmds.cli
    ~~~~~~~~

    Command line interface for use with markdownclerk.

    :copyright: (c) 2016 by John P. Neumann.
    :license: MIT, see LICENSE for more details.
"""
from __future__ import absolute_import

import os
import logging

import click

from .. import __version__ as version
from ..clerks import project


LOGGER = logging.getLogger(__name__)
DEFAULT_TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))


@click.group()
@click.version_option(version, help="Print the version number and exit.")
def markdownclerk():
    """MarkdownClerk CLI allows you to specify configurable input prompts to build extensible markdown templates that
    will generate the data based on the inputs received."""
    pass  # pragma: no cover


@markdownclerk.command()
@click.argument('location', type=click.Path(file_okay=False, dir_okay=True))
@click.option('template_file', '--template-file',
              default=os.path.join(DEFAULT_TEMPLATE_PATH, 'project', 'default.md'),
              type=click.Path(file_okay=True, exists=True, readable=True),
              help="The template file to use for generation.")
@click.option('config_file', '--config-file', default=os.path.join(DEFAULT_TEMPLATE_PATH, 'project', 'settings.yml'),
              type=click.Path(file_okay=True, exists=True, readable=True),
              help="The configuration file with the relevant prompts for the markdown.")
def time_based_project(location, template_file, config_file):
    """Generate a project for a given time period, based on the template configuration.

    \b
    location (:obj:`str`): Where to create the project structure.

    """
    if project.generate_project_daily(location, template_file, config_file):
        raise click.UsageError('There was ane error generating your project')


if __name__ == "__main__":
    markdownclerk()
