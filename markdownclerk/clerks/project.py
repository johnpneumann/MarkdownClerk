# -*- coding: utf-8 -*-
"""
    clerks.project
    ~~~~~~~~~~~~~~

    Generate the markdown files for a project.

    :copyright: (c) 2016 by John P. Neumann.
    :license: MIT, see LICENSE for more details.
"""
import io
import os
import logging

import yaml
from boltons import fileutils
from jinja2 import Environment, FileSystemLoader


LOGGER = logging.getLogger(__name__)


def generate_project_daily(location, template_file, settings_file):
    """Generate a new file for each day of the project.

    Args:
        location (:obj:`str`): The location for the project structure.
        template_file (:obj:`str`): The template file to use for the generation.
        settings_file (:obj:`str`): The settings file to use for the markdown.

    Returns:
        int: Status code of success or failure. Anything except 0 is a failure.

    """
    with io.open(settings_file) as fopen:
        data = yaml.safe_load(fopen.read())
    project_vars = data['vars']
    weeks = data['settings']['weeks']
    days = 7 if data['settings']['days'] > 7 else data['settings']['days']

    template_dir = os.path.dirname(template_file)
    jinja_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
    template = jinja_env.get_template(os.path.basename(template_file))
    for week in range(1, weeks + 1):
        LOGGER.info('Generating week %s files', week)
        for day in range(1, days + 1):
            day_path = os.path.join(location, 'week{:02d}'.format(week), 'day{:02d}'.format(day))
            if _create_dir(day_path):
                return 1
            readme_path = os.path.join(day_path, 'README.md')
            try:
                with fileutils.atomic_save(readme_path) as fopen:
                    fopen.writelines(template.render(**project_vars).encode('utf-8'))
            except (OSError, IOError):
                LOGGER.exception('Failed to write data to %s', readme_path, exc_info=True)
                return 1
    return 0


def _create_dir(directory_path):
    """Create a directory for us.

    Args:
        directory_path (:obj:`str`): The path to the directory to create.

    Returns:
        int: Status code of success or failure. Anything except 0 is a failure.

    """
    try:
        fileutils.mkdir_p(directory_path)
    except OSError:
        LOGGER.exception('Could not create directory: %s', directory_path, exc_info=True)
        return 1
    return 0
