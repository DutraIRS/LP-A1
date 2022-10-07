import scrape
from bs4 import BeautifulSoup
import pandas as pd
import re

def obtem_span_premios(url):
    """Obtém a tag span que contém o título da seção de prêmios da Wikipedia

    :param url: URL do site em que a tag será buscada
    :type url: str
    :return: A tag span ou None se não for encontrada
    :rtype: bs4.element.Tag/None
    """
    site = scrape.pegar_html(url)
    bs = BeautifulSoup(site, 'html.parser')

    return bs.find(id = "Awards_and_nominations")

def obtem_premiacoes(url):
    """Obtém as premiações da banda Guns N' Roses da Wikipedia

    :param url: URL do site em que as premiações serão buscadas
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
                    texto = "".join(child.strings)

                    ano, info = texto.split(":")

                    # Separa a string que usa algum dos hífens
                    separado = re.split("-|–", info)

                    descricao = separado[0].strip()

                    if len(separado) > 1:
                        # O texto após o hífen é o que está sendo premiado
                        premiado = separado[1].strip("\" ")
                    else:
                        # Se não há hífen, então a própria banda que está sendo premiada
                        premiado = "Guns N' Roses"
                    
                    dados.append([nome_premiacao, descricao, premiado, int(ano)])
    
    colunas = ["Nome Premiação", "Descrição", "Premiado", "Ano"]

    return pd.DataFrame(data = dados, columns = colunas)