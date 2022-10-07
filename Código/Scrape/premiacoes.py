import scrape
from bs4 import BeautifulSoup

def obtem_span_premios(url):
    """Obtém a tag span que contém o título da seção de prêmios

    :param url: URL do site em que a tag será buscada
    :type url: str
    :return: A tag span ou None se não for encontrada
    :rtype: bs4.element.Tag/None
    """
    site = scrape.pegar_html(url)
    bs = BeautifulSoup(site, 'html.parser')

    return bs.find(id = "Awards_and_nominations")