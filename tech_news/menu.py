import sys
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_tag,
    search_by_category,
    search_by_date
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.scraper import get_tech_news


def tech_news():
    amount = input('Digite quantas notícias serão buscadas:')

    if not amount.isdigit():
        raise ValueError('Erro: valor não numérico')

    return get_tech_news(int(amount))


def title():
    title = input('Digite o título:')
    return search_by_title(title)


def date():
    date = input('Digite a data no formato aaaa-mm-dd:')
    return search_by_date(date)


def tag():
    tag = input('Digite a tag:')
    return search_by_tag(tag)


def category():
    category = input('Digite a categoria:')
    return search_by_category(category)


def five_top_news():
    return top_5_news()


def five_top_categories():
    return top_5_categories()


list_functions = [
    tech_news, title, date, tag, category, five_top_news, five_top_categories
]


# Requisito 12
def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    response = ''
    if option and int(option) < 7:
        response = list_functions[int(option)]()
    elif option == '7':
        print('Encerrando script\n')
    else:
        print('Opção inválida', file=sys.stderr)

    print(response, end="")
    return response
