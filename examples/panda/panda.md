## I'm Grateful For
{% for number in range(1, grateful+1) %}
{{ number }}.
{% endfor %}

## Today Will Be Great Because
{% for number in range(1, great_because+1) %}
{{ number }}.
{% endfor %}

{% if affirmation %}
## Affirmation
{% endif %}

{% if focus %}
## Focus
{% endif %}

{% if focus %}
## Exercise
{% endif %}

{% for task in range(1, priority_count + 1) %}
{{ task }}.
{% endfor %}

{% if eodnotes %}
## EOD Notes
{% for note in eodnotes %}
### {{ note }}
{% endfor %}
{% endif %}
