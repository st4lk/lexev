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

- dropnroll.tv
- wirelayer.net
- fursk.ru
- 3dplitka.ru
- woobie.ru


Open-source contributing:

- django-solid-i18n-urls
- django-affiliate
- django-oscar
- acl_webapp
- others
{% endif %}

{% endfor %}

Education
=========

{% for e in linkedin['educations']['values'] %}{% if e.schoolName %}
### {{ e.schoolName }} ({{e.startDate.year}} - {{e.endDate.year}})

{{ e.degree }}, {{ e.fieldOfStudy }}
{% endif %}{% endfor %}

Certifications
==============

{% for cert in linkedin['certifications']['values'] %}
 - {{ cert.name }}{% if 'C100DEV' in cert.name %}, license 746-203-198{% endif %}
{% endfor %}

Links
=====
{% include 'includes/links.md' %}
