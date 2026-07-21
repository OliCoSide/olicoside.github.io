---
layout: archive
title: "LinkedIn"
permalink: /linkedin/
author_profile: true
---

{% include base_path %}

I share research updates, conference notes, and thoughts on fairness in insurance on LinkedIn. Below is a selection of my posts — you can find all of them on my activity feed.

<a href="https://www.linkedin.com/in/olivier-cote-act/recent-activity/all/" class="btn btn--linkedin"><i class="fab fa-fw fa-linkedin" aria-hidden="true"></i> See all my posts on LinkedIn</a>

{% assign posts = site.data.linkedin_posts.posts %}
{% if posts and posts.size > 0 %}
<div class="linkedin-grid">
  {% for post in posts %}
    {% if post.embed %}
      {% assign embed_url = post.embed %}
    {% else %}
      {% assign activity_id = post.url | split: "activity-" | last | split: "-" | first %}
      {% assign embed_url = "https://www.linkedin.com/embed/feed/update/urn:li:activity:" | append: activity_id %}
    {% endif %}
    <div class="linkedin-grid__item">
      <iframe src="{{ embed_url }}" frameborder="0" allowfullscreen="" title="Embedded LinkedIn post" loading="lazy"></iframe>
      {% if post.note %}<p class="linkedin-grid__note">{{ post.note }}</p>{% endif %}
    </div>
  {% endfor %}
</div>
{% else %}
<p class="notice">Featured posts are coming soon — in the meantime, everything is on <a href="https://www.linkedin.com/in/olivier-cote-act/recent-activity/all/">my LinkedIn activity feed</a>.</p>
{% endif %}
