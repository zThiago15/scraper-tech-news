from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    return search_news(title)


# Requisito 7
def search_by_date(date: str):
    try:
        formated_date = datetime(date).strftime('%d/%m/%y')
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
    """Seu código deve vir aqui"""
