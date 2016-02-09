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
