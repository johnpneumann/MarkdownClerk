#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate our project Markdown files.

.. module:: markdownclerk.clerk
    :platform: Linux, MacOS, Windows

.. moduleauthor:: johnpneumann

.. note::
    None
"""
# Built In
import os

# Third Party
import yaml
import click
from boltons import fileutils
from jinja2 import Environment, FileSystemLoader

# Custom


DEFAULT_TEMPLATE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates', 'default.md'))
DEFAULT_SETTINGS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates', 'settings.yml'))


@click.command()
@click.version_option()
@click.argument('location', type=click.Path(file_okay=False, dir_okay=True))
@click.option('template_file', '--template-file', default=DEFAULT_TEMPLATE_FILE, type=click.Path(file_okay=True, exists=True, readable=True), help="The template file to use for generation.")
@click.option('settings_file', '--settings-file', default=DEFAULT_SETTINGS_FILE, type=click.File('rb'), help="The settings file to use for the markdown.")
def main(location, template_file, settings_file):
    """Generate a new file for us to work with.

    \b
    :param location: Where to create the project structure.
    :type location: str/path
    :returns: None

    """
    data = yaml.safe_load(settings_file)
    settings = data['settings']
    project_vars = data['vars']
    weeks = settings['weeks']
    days = 7 if settings['days'] > 7 else settings['days']

    if not os.path.exists(location):
        fileutils.mkdir_p(location)
    template_dir = os.path.dirname(template_file)
    template_name = os.path.basename(template_file)
    jinja_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
    template = jinja_env.get_template(template_name)
    with click.progressbar(length=sum([weeks, days]), label='Creating structure') as progbar:
        for week in range(1, weeks + 1):
            pth = os.path.join(location, 'week{:02d}'.format(week))
            fileutils.mkdir_p(pth)
            for day in range(1, days + 1):
                daynum = 'day{:02d}'.format(day)
                day_pth = os.path.join(pth, daynum)
                fileutils.mkdir_p(day_pth)
                template_data = template.render(**project_vars).encode('utf-8')
                with fileutils.atomic_save(os.path.join(day_pth, 'README.md')) as fopen:
                    fopen.writelines(template_data)
                progbar.update(week + day)


if __name__ == "__main__":
    main()
