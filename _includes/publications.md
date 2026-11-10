## Publications

{% for pub in site.data.publications.papers %}
<div class="pub">
  <div class="pub-title">{{ pub.title }}</div>
  <div class="pub-authors">{{ pub.authors }}</div>
  <div class="pub-venue">{{ pub.venue }}</div>
  <div class="pub-links">
    {% if pub.arxiv %}<a href="{{ pub.arxiv }}" target="_blank" rel="noopener" aria-label="arXiv" title="arXiv">{% include icons/arxiv.svg %}</a>{% endif %}
    {% if pub.pdf %}<a href="{{ pub.pdf }}" target="_blank" rel="noopener" aria-label="PDF" title="PDF">{% include icons/pdf.svg %}</a>{% endif %}
    {% if pub.code %}<a href="{{ pub.code }}" target="_blank" rel="noopener" aria-label="Code" title="Code">{% include icons/code.svg %}</a>{% endif %}
    {% if pub.page %}<a href="{{ pub.page }}" target="_blank" rel="noopener" aria-label="Project page" title="Project page">{% include icons/page.svg %}</a>{% endif %}
    {% if pub.bibtex %}<a href="{{ pub.bibtex }}" target="_blank" rel="noopener" aria-label="BibTeX" title="BibTeX">{% include icons/bibtex.svg %}</a>{% endif %}
  </div>
</div>
{% endfor %}
