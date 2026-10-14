## Publications

{% for group in site.data.publications.groups %}{% if group.items and group.items != empty %}
<h3 class="pub-group">{{ group.name }}</h3>

{% for pub in group.items %}
<div class="pub">
  <div class="pub-title">{{ pub.title }}</div>
  <div class="pub-authors">{{ pub.authors }}</div>
  <div class="pub-venue">{{ pub.venue }}</div>
  <div class="pub-links">
    {% if pub.arxiv %}<a href="{{ pub.arxiv }}" target="_blank" rel="noopener">arXiv</a>{% endif %}
    {% if pub.pdf %}<a href="{{ pub.pdf }}" target="_blank" rel="noopener">PDF</a>{% endif %}
    {% if pub.code %}<a href="{{ pub.code }}" target="_blank" rel="noopener">Code</a>{% endif %}
    {% if pub.page %}<a href="{{ pub.page }}" target="_blank" rel="noopener">Project Page</a>{% endif %}
    {% if pub.bibtex %}<a href="{{ pub.bibtex }}" target="_blank" rel="noopener">BibTeX</a>{% endif %}
  </div>
</div>
{% endfor %}
{% endif %}{% endfor %}
