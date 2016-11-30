{% if project_name %}
# {{ project_name }}
What are we accomplishing for {{ project_name }} today?
{% endif %}

{% if task_count %}
## Day {{ day }}
{% for task in range(task_count) %}
- [ ] TBD
{% endfor %}
{% endif %}

{% if eod_questions %}
## EOD Reflection
{% for note in eod_questions %}
### {{ note }}

{% endfor %}
{% endif %}
