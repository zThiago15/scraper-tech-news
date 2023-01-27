from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {'title', {'$regex': title, '$options': 'i'}}
    return [(new["title"], new["url"]) for new in search_news(query)]


# Requisito 7
def search_by_date(date: str):
    try:
        formated_date = datetime.fromisoformat(date).strftime('%d/%m/%y')
        query = {'timestamp': {'$eq': formated_date}}
        return [(new['title'], new['url']) for new in search_news(query)]

    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    query = {'tags': {'$regex': tag, '$options': 'i'}}
    return [(new['title'], new['url']) for new in search_news(query)]


# Requisito 9
def search_by_category(category):
    query = {'category': {'$regex': category, '$options': 'i'}}
    return [(new['title'], new['url']) for new in search_news(query)]
