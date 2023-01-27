import sys
from tech_news.database import create_news, search_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def database():
    data = input('news quantity to register:')
    return create_news(data)


def title():
    title = input('type the news title:')
    return search_by_title(title)


def tag():
    tag = input('type the news tag')
    return search_by_tag(tag)


def category():
    category = input('type the category')
    return search_by_category(category)


def five_top_news():
    return top_5_news


def five_top_categories():
    return top_5_categories


list_functions = [
    database, title, tag, category, five_top_news, five_top_categories
]


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    option = int(input(
        "Selecione uma das opções a seguir:\n"
        "0 - Popular o banco com notícias;\n"
        "1 - Buscar notícias por título;\n"
        "2 - Buscar notícias por data;\n"
        "3 - Buscar notícias por tag;\n"
        "4 - Buscar notícias por categoria;\n"
        "5 - Listar top 5 notícias;\n"
        "6 - Listar top 5 categorias;\n"
        "7 - Sair."
    ))

    if option < 7:
        list_functions[option]()
    elif option == '7':
        print('finishing process')
    else:
        print('Opção inválida', file=sys.stderr)
