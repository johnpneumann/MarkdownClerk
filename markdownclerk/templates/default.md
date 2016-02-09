{% if projectname %}
# {{ projectname }}
What are we accomplishing for {{ projectname }} today?
{% endif %}

{% if taskcount %}
## Day {{ day }}
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
