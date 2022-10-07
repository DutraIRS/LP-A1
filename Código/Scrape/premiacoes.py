import scrape
import bs4
import pandas as pd
import re


def obtem_span_premios(url: str):
    """Obtém a tag span que contém o título da seção de prêmios da Wikipedia

    :param url: URL da página da Wikipedia em que a tag será buscada
    :type url: str
    :return: A tag span ou None se não for encontrada
    :rtype: bs4.element.Tag/None
    """
    site = scrape.pegar_html(url)
    bs = bs4.BeautifulSoup(site, 'html.parser')

    return bs.find(id="Awards_and_nominations")


def ler_premiacao(tag_li: bs4.element.Tag):
    """Obtém descrição, premiado e ano de premiação de uma tag li da Wikipedia

    :param tag_li: Tag li que contém as informações da premiação
    :type tag_li: bs4.element.Tag
    :return: Lista contendo as informações lidas
    :rtype: list[str]
    """
    texto = "".join(tag_li.strings)

    # O ano é separado por ":"
    ano, info = texto.split(":")

    # A descrição é separada do premiado por hífen
    separado = re.split("-|–", info)
    descricao = separado[0].strip()

    if len(separado) > 1:
        # O texto após o hífen é o que está sendo premiado
        premiado = separado[1].strip("\" ")
    else:
        # Se não há hífen, então é a própria banda que está sendo premiada
        premiado = "Guns N' Roses"
    
    return [descricao, premiado, ano]


def obtem_premiacoes(url: str):
    """Obtém as premiações da banda Guns N' Roses da Wikipedia

    :param url: URL da Wikipedia em que as premiações serão buscadas
    :type url: str
    :return: DataFrame contendo o nome, descrição, ano e o que é premiado
    :rtype: pandas.core.frame.DataFrame
    """
    # Obtém a tag h2 que contém o span, que está no mesmo nível das premiações
    h2_premios = obtem_span_premios(url).parent

    dados = []

    for elemento in h2_premios.next_siblings:
        match elemento.name:
            # tag h2: início de outra seção, acabou a seção de prêmios
            case "h2":
                break

            # tag p: início da listagem de premiações de um mesmo evento
            case "p":
                # Obtém o nome do evento
                nome_premiacao = elemento.find("a").string

            # tag ul: inicia uma lista de premiações
            case "ul":
                for child in elemento.find_all("li"):
                    infos = ler_premiacao(child)

                    dados.append([nome_premiacao] + infos)

    colunas = ["Nome Premiação", "Descrição", "Premiado", "Ano"]

    return pd.DataFrame(data=dados, columns=colunas)