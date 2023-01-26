import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if (response.status_code == 200):
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    sel = Selector(text=html_content)
    urls = sel.css('h2.entry-title a::attr(href)').getall()

    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(text=html_content)
    next_page_url = sel.css('a.next::attr(href)').get()
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    sel = Selector(text=html_content)

    return {
        "url": sel.css('link[rel=canonical]::attr(href)').get(),
        "title": sel.css('h1.entry-title::text').get().strip(),
        "timestamp": sel.css('li.meta-date::text').get(),
        "writer": sel.css('a.url.fn.n::text').get(),
        "comments_count": sel.css('.post-comments-simple h5::text').get() or 0,
        "summary": sel.xpath('string(//p)').get().strip(),
        "tags": sel.css('.post-tags a::text').getall(),
        "category": sel.css('.meta-category span.label::text').get()
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
