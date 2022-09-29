import pandas as pd
from bs4 import BeautifulSoup
import requests

def pegar_html(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o html e retorna uma string 
    referente a página dada pela url

	:param url: Link da página da internet que se deseja buscar o html
	:url type: str
	:return: Texto do html do link dado
	:r type: str
	'''

    texto_html = requests.get(url)
    return texto_html.text

def pegar_letra(url: str):
    '''
	A função recebe um url do site lyrics.com, busca a letra da música que está presente
    nesse html e retorna uma string referente a letra dessa música

	:param url: Link da página da música
	:url type: str
	:return: letra da música
	:r type: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    letra = soup.find('pre', id='lyric-body-text')
    
    try:
        return letra.text
    except:
        print('Letra não encontrada')

def pegar_letras_musicas_album(url: str):
    '''
	A função recebe um url do site lyrics.com, busca as letras de todas as músicas
    desse album e retorna uma lista com essas músicas

	:param url: Link da página do álbum escolhido
	:url type: str
	:return: Letras das músicas do álbum
	:r type: list
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_letras = []

    #dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_letra' para pegar a letra de cada uma das músicas
        for a in links:
            letra_album = "https://www.lyrics.com/" + a['href']
            print('pegando a letra da música: ', "https://www.lyrics.com/" + a['href'])

            #O site usado dá um erro em momentos aleatórios onde não há conteúdo no link
            #Para resolver esse problema usaremos um while, toda vez que o site estiver
            #Vazio o programa fará a busca novamente, corrigindo o problema.
            verso = None
            while verso == None:
                verso = pegar_letra(letra_album)

            #Removeremos da letra os '\n' '\r' e sinalização de refrão '[Chorus:]' mantendo apenas a letra da música
            lista_letras.append(verso.replace('\n', ' ').replace('\r', '').replace('[Chorus:] ', ''))

        return lista_letras

def pegar_titulo(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o nome da música que está
    presente nesse link o retorna

	:param url: Link da página da música
	:url type: str
	:return: Título da música
	:r type: str
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    titulo = soup.find('h1', id='lyric-title-text')
    try:
        return titulo.text
    except:
        print('erro')

def pegar_titulos_musicas_album(url: str):
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_titulos = []

    #semelhante à função 'pegar_letras_musicas_album' dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_titulo' para pegar a letra de cada uma das músicas
        for a in links:
            letra_album = "https://www.lyrics.com/" + a['href']
            print('pegando o título da música: ', "https://www.lyrics.com/" + a['href'])

            #Uso do while para evitar o erro da página vazia novamente
            titulos = None
            while titulos == None:
                titulos = pegar_titulo(letra_album)

            lista_titulos.append(titulos.replace('\n', ' ').replace('\r', '').replace('[Chorus:] ', ''))
        return lista_titulos

def pegar_tempo_musicas_album(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o tempo de todas as músicas
    desse álbum e retorna uma lista com esses tempos

	:param url: Link da página da música
	:url type: str
	:return: Tempo das músicas do álbum
	:r type: list
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    for div in album:
        tempo_td = div.find_all('td', attrs={'class': 'tal qx fsl'})
        lista_tempos = []

        #Os tempos das músicas estão localizados em uma tabela 'td' de classe 'tal qx fsl'
        #Especificamente na quarta coluna então usando um contador obteremos todos os conteúdos
        #Que estão na quarta coluna.
        count = 1
        for tem in tempo_td:
            if count % 4 == 0:
                lista_tempos.append(tem.text)
            count += 1
        
        return lista_tempos

def gerar_dataframe_album(url: str):
    '''
    Usando as funções criadas obteremos um dataframe de um álbum dado a partir de
    um url do site lyrics.com
    
	:param url: Link da página da música
	:url type: str
	:return: Dataframe do álbum
	:r type: DataFrame
    '''
    print('O processo pode demorar um pouco dependendo da quantidade de músicas. Aguarde...')
    dados = {'Tempo':pegar_tempo_musicas_album(url), 'letra':pegar_letras_musicas_album(url)}
    df = pd.DataFrame(data=dados, index=[pegar_titulos_musicas_album(url)])
    print(df)
    return df

print(type(gerar_dataframe_album('https://www.lyrics.com/album/571148/G-N%27-R-Lies-Appetite-for-Destruction')))
#se quiser testa esse também https://www.lyrics.com/album/571148/G-N%27-R-Lies-Appetite-for-Destruction
