.. _usage:

Usage
=====

Basic usage of MarkdownClerk can be found below.

.. toctree::

Running
-------
Running it is as simple as:

.. code:: sh

   clerk /path/to/where/you/want/the/project


To see the help:

.. code:: sh

   clerk --help

allthethings

.. code:: sh

   clerk /path/to/project --template-file /path/to/template/foo.md --settings-file /path/to/foo.yml

Configuration
-------------
Configuration consists of a yaml file and a template file,
to consume said yaml file, which is a jinja template.


Settings File
+++++++++++++

The settings file is a ``yaml`` file and must have two things defined:
``settings`` and ``vars``.

``settings`` must include ``weeks`` and ``days`` (which represent how many weeks
the project lasts and how many days of the week you'll be working on it).

``vars`` holds arbitrary data that's specifically related to your template
file (which is a jinja template).

.. code:: yaml

   ---
   settings:
       weeks: 1
       days: 5

   vars:
       projectname: SpongeBob
       taskcount: 3
       eodnotes:
         - Was it the best day ever?
         - Did you spend any time with Gary?
         - Is Patrick still your best friend?

Template File
+++++++++++++

The template file correlates with the ``vars`` that exist in the
``settings`` file.

.. code::

   # {{ projectname }}
   Is it the best day ever?

   ## Day {{ day }}
   {% if taskcount %}
   {% for task in range(taskcount) %}
   - [ ] TBD
   {% endfor %}
   {% endif %}

   {% if eodnotes %}
   ## EOD Notes
   {% for note in eodnotes %}
   ### {{ note }}

   {% endfor %}
   {% endif %}
