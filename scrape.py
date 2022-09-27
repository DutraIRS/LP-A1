import pandas as pd
from bs4 import BeautifulSoup
import requests

def pegar_html(url: str):
    texto_html = requests.get(url)
    return texto_html.text

def pegar_letra(url: str):
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    letra = soup.find('pre', id='lyric-body-text')
    try:
        return letra.text
    except:
        print('erro')

def pegar_letras_musicas_album(url: str):
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_letras = []

    for div in album:
        links = div.find_all('a')
        for a in links:
            print('buscando a letra do segunte link', "https://www.lyrics.com/" + a['href'])
            letra_album = "https://www.lyrics.com/" + a['href']

            verso = None
            while verso == None:
                verso = pegar_letra(letra_album)

            lista_letras.append(verso.replace('\n', ' ').replace('\r', '').replace('[Chorus:] ', ''))

        return lista_letras

def pegar_nome_musica(url: str):
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    titulo = soup.find('h1', id='lyric-title-text')
    try:
        return titulo.text
    except:
        print('erro')

def pegar_nomes_musicas_album(url: str):
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_titulos = []

    for div in album:
        links = div.find_all('a')
        for a in links:
            print('buscando o nome da música no segunte link', "https://www.lyrics.com/" + a['href'])
            letra_album = "https://www.lyrics.com/" + a['href']

            titulos = None
            while titulos == None:
                titulos = pegar_nome_musica(letra_album)

            lista_titulos.append(titulos.replace('\n', ' ').replace('\r', '').replace('[Chorus:] ', ''))

        return lista_titulos

def pegar_tempo_musicas_album(url: str):
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    for div in album:
        tempo_td = div.find_all('td', attrs={'class': 'tal qx fsl'})
        lista_tempos = []

        count = 1
        for tem in tempo_td:
            if count % 4 == 0:
                lista_tempos.append(tem)
            count += 1
        print(lista_tempos)
        return lista_tempos

def gerar_dataframe_album(url: str):
    dados = {'Tempo':pegar_tempo_musicas_album(url), 'letra':pegar_letras_musicas_album(url)}
    df = pd.DataFrame(data=dados, index=[pegar_nomes_musicas_album(url)])
    print(df)
    return df

gerar_dataframe_album('https://www.lyrics.com/album/571148/G-N%27-R-Lies-Appetite-for-Destruction')
#se quiser testa esse também https://www.lyrics.com/album/571148/G-N%27-R-Lies-Appetite-for-Destruction