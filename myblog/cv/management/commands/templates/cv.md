Summary
=======

Alexey Evseev, web developer based in Moscow, Russia. 

{{ linkedin.summary }}

Tools and technologies
======================

{% include 'includes/tools_and_technologies.md' %}

Experience
==========

{% for p in linkedin['positions']['values'] %}
### {{ p.company.name }} ({{p.startDate.year}}.{{"{0:0>2}".format(p.startDate.month)}} - {% if p.isCurrent %}Present{% else %}{{p.endDate.year}}.{{"{0:0>2}".format(p.endDate.month)}}{% endif %})
_{{ p.title }}_

{{ p.summary }}
{% if 'additional' in p %}

{{ p.additional }}
{% endif %}

{% endfor %}

Education
=========

{% for e in linkedin['educations']['values'] %}
### {{ e.schoolName }} ({{e.startDate.year}} - {{e.endDate.year}})

{{ e.degree }}, {{ e.fieldOfStudy }}
{% endfor %}

Courses
=======

{% for c in linkedin['courses']['values'] %}
 - {{ c.name }}
{% endfor %}

Links
=====
{% include 'includes/links.md' %}
