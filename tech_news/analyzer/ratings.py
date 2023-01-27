from tech_news.database import find_news
from collections import Counter


def sort_by_comment(e):
    return e["comments_count"]


# Requisito 10
def top_5_news():

    # news = find_news()
    # five_news = news.sort(key=e['comments_count'], reverse=True)
    # return [(new['title'], new['url']) for new in five_news]
    news = find_news()
    news.sort(key=sort_by_comment, reverse=True)
    if len(news) > 5:
        news = news[:5]
    list_formated = []
    for news in news:
        list_formated.append((news["title"], news["url"]))
    return list_formated


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = [new["category"] for new in news]
    categories_count = Counter(sorted(categories)).most_common()
    categories_top_five = [category[0] for category in categories_count]
    return categories_top_five[:5]
