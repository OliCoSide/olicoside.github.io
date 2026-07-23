---
layout: archive
title: "Event organization"
permalink: /events/
author_profile: true
---

{% include base_path %}

{% assign up = site.data.events.upcoming %}
{% assign past = site.data.events.past %}

{% if up and up.size > 0 %}
<section class="events-box events-box--upcoming">
  <h2 class="events-box__label">Upcoming</h2>
  {% for e in up %}
  <div class="events-box__entry">
    <p class="events-box__title">{% if e.url %}<a href="{{ e.url }}">{{ e.title }}</a>{% else %}{{ e.title }}{% endif %}</p>
    <p class="paper-authors">{% if e.role %}{{ e.role }}{% endif %}{% if e.date %} · {{ e.date }}{% endif %}{% if e.location %} · {{ e.location }}{% endif %}</p>
  </div>
  {% endfor %}
</section>
{% endif %}

{% if past and past.size > 0 %}
<section class="events-box events-box--past">
  <h2 class="events-box__label">Past</h2>
  {% for e in past %}
  <div class="events-box__entry">
    <p class="events-box__title">{% if e.url %}<a href="{{ e.url }}">{{ e.title }}</a>{% else %}{{ e.title }}{% endif %}</p>
    <p class="paper-authors">{% if e.role %}{{ e.role }}{% endif %}{% if e.date %} · {{ e.date }}{% endif %}{% if e.location %} · {{ e.location }}{% endif %}</p>
  </div>
  {% endfor %}
</section>
{% endif %}

{% if up.size == 0 and past.size == 0 %}
<p>Coming soon.</p>
{% endif %}
