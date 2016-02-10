# MarkdownClerk
Markdown Clerk is a simple project tracker that
generates markdown files in a structured way.

## Installation
The easiest way is to:
```
git clone https://github.com/johnpneumann/MarkdownClerk.git
pip install MarkdownClerk
```

## Running
Running it is as simple as: `clerk /path/to/where/you/want/the/project`

To see the help: `clerk --help`

:allthethings:
`clerk /path/to/project --template-file /path/to/template/foo.md --settings-file /path/to/foo.yml`

## Examples
Check the examples directory... For examples.

## Configuration
### Settings File
The settings file is a `yaml` file and must have two
things defined: `settings` and `vars`.

`settings` must include `weeks` and `days` (which
represent how many weeks the project lasts and how many
days of the week you'll be working on it).

`vars` holds arbitrary data that's specifically related
to your template file (which is a jinja template).

```
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
```

### Template File
The template file correlates with the `vars`
that exist in the `settings` file.

```
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
```

## Why
I needed a way to generate easily digestable tasks
each day for a large project. I found that giving
myself a limited amount of tasks in a standard and
configurable format allowed me to track towards my
goals easily, without distracting from my ultimate
goal. I set other restrictions as well, such as
not carrying any tasks over from previous days or
making todo lists with tasks for the next day,
forcing myself to start fresh every day.

## License
MIT
