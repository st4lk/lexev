Summary
=======

Alexey Evseev, web developer based in Moscow, Russia.<br/>Date of Birth: 06.02.1985

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
{% if p.company.name == 'Freelance' %}

Projects, i've been involved to:

- fursk.ru
- dropnroll.tv
- courses.by
- wirelayer.net
- 3dplitka.ru
- tvoya.mechta.ru


Open-source contributing:

- django-oscar
{% endif %}

{% endfor %}

Education
=========

{% for e in linkedin['educations']['values'] %}
### {{ e.schoolName }} ({{e.startDate.year}} - {{e.endDate.year}})

{{ e.degree }}, {{ e.fieldOfStudy }}
{% endfor %}

Certifications
==============

{% for cert in linkedin['certifications']['values'] %}
 - {{ cert.name }}{% if 'C100DEV' in cert.name %}, license 746-203-198{% endif %}
{% endfor %}

Courses
=======

{% for c in linkedin['courses']['values'] %}
 - {{ c.name }}
{% endfor %}

Links
=====
{% include 'includes/links.md' %}
