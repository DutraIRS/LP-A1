from faulthandler import dump_traceback_later
import pandas as pd
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import requests

def pegar_html(url: str):
    '''A função recebe um url do site lyrics.com, busca o html e retorna uma string 
    referente a página dada pela url

	:param url: Link da página da internet que se deseja buscar o html
	:url type: str
	:return: Texto do html do link dado
	:rtype: str
	'''

    texto_html = requests.get(url)
    return texto_html.text

def pegar_letra(url: str):
    '''A função recebe um url do site lyrics.com, busca a letra da música que está presente
    nesse html e retorna uma string referente a letra dessa música

	:param url: Link da página da música
	:url type: str
	:return: letra da música
	:rtype: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    letra = soup.find('pre', id='lyric-body-text')
    
    try:
        return letra.text
    except:
        print('Letra não encontrada')

def pegar_letras_musicas_album(url: str):
    '''A função recebe um url do site lyrics.com referente ao álbum de uma banda,
    busca as letras de todas as músicas desse album e retorna uma lista com essas 
    músicas

	:param url: Link da página do álbum
	:url type: str
	:return: Letras das músicas do álbum
	:rtype: list
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
            print('procurando letra no link: ', "https://www.lyrics.com/" + a['href'])

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
    '''A função recebe um url do site lyrics.com, busca o nome da música que está
    presente nesse link o retorna

	:param url: Link da página da música
	:url type: str
	:return: Título da música
	:rtype: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    titulo = soup.find('h1', id='lyric-title-text')
    try:
        return titulo.text
    except:
        print('erro')

def pegar_titulos_musicas_album(url: str):
    '''A função recebe um url do site lyrics.com referente ao álbum de uma banda, busca 
    os títulos de todas as músicas desse álbum e retorna uma lista com esses títulos

	:param url: Link da página do álbum
	:url type: str
	:return: Títulos das músicas do álbum
	:rtype: list
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_titulos = []

    #semelhante à função 'pegar_letras_musicas_album' dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_titulo' para pegar o título de cada uma das músicas
        for a in links:
            letra_album = "https://www.lyrics.com/" + a['href']
            print('procurando título no link: ', "https://www.lyrics.com/" + a['href'])

            #Uso do while para evitar o erro da página vazia novamente
            titulos = None
            while titulos == None:
                titulos = pegar_titulo(letra_album)

            lista_titulos.append(titulos.replace('\n', ' ').replace('\r', '').replace('[Chorus:] ', ''))
        return lista_titulos

def pegar_ano(url: str):
    '''A função recebe um url do site lyrics.com, busca o ano de lançamento da música que está presente
    nesse link e retorna uma string referente ao seu ano de lançamento
    
	:param url: Link da página da música
	:url type: str
	:return: Ano de lançamento
	:rtype: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    tempo_ano = soup.findAll('dd', attrs={'class': 'dd-margin'})

    #O ano de lançamento da música se encontra em uma lista, sendo ele o primeiro elemento
    tempo_ano_list = []
    for item in tempo_ano:
        tempo_ano_list.append(item)
    try:
        tempo = tempo_ano_list[0]
    except:
        tempo = None
    
    try:
        return tempo.text
    except:
        return None

def pegar_ano_musicas_album(url: str):
    '''A função recebe um url do site lyrics.com referente ao álbum de uma banda, busca
    o tempo de todas as músicas desse álbum e retorna uma lista com esses tempos

	:param url: Link da página do álbum
	:url type: str
	:return: Tempo das músicas do álbum
	:rtype: list
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_tempos = []

    #dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_ano' para pegar o ano de lançamento de cada uma das músicas
        for a in links:
            tempo_album = "https://www.lyrics.com/" + a['href']
            print('procurando tempo no link: ', "https://www.lyrics.com/" + a['href'])
            
            time = pegar_ano(tempo_album)
            lista_tempos.append(time)

    return lista_tempos
        
def pegar_titulo_album(url: str):
    '''A função recebe um url do site lyrics.com referente ao album de uma banda, busca o título
    desse álbum e o retorna

	:param url: Link da página do álbum
	:url type: str
	:return: Título do álbum
	:rtype: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.find('h1')

    titulo_album = album.text
    return titulo_album.replace(' Album', '').replace(' [edited]', '')

def pegar_compositores(url: str):
    '''A função recebe um url do site lyrics.com, busca o(s) compositor(es) da música desse desse url
    e retorna o(s) seu(s) nome(s)

	:param url: Link da página da música
	:url type: str
	:return: Compositores da música
	:rtype: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    detalhes = soup.find('div', attrs={'class': 'lyric-credits'})
    
    itens = detalhes.find('p', attrs={'class': False})
    compositores = itens.text
    
    return compositores.replace('Written by: ', '')

def pegar_compositores_musicas_album(url: str):
    '''A função recebe um url do site lyrics.com referente ao álbum de uma banda, busca 
    os compositores de todas as músicas desse álbum e retorna uma lista com esses compositores

	:param url: Link da página do álbum
	:url type: str
	:return: Compositores das músicas do álbum
	:rtype: list
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_compositores = []

    #dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_compositores' para pegar os compositores de cada uma das músicas
        for a in links:
            compositores_album = "https://www.lyrics.com/" + a['href']
            print('procurando compositores no link: ', "https://www.lyrics.com" + a['href'])
            
            compositores = pegar_compositores(compositores_album).replace('(USA 2) ', '').replace('(usa 2) ', '')
            lista_compositores.append(compositores)
    return lista_compositores

def pegar_duracao_musicas_album_spotify(spotify_id: str):
    '''A função recebe um url do site pt.wikipedia.org, busca as durações das músicas
    do álbum naquele link e retorna uma lista com essas durações
    
	:param url: Link da página do álbum (wikipédia)
	:url type: str
	:return: Lista com a duração das músicas
	:rtype: list
    '''

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='1a9faa80969a428cae902caf7caa6402', client_secret='d4ec70ec23114cd8a19b7b4dcf51aa62'))

    results = spotify.album_tracks(spotify_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results)

    lista_popularidade = []

    for track in tracks:
        track_id = track['id']
        track_page = spotify.track(track_id)
        duration = track_page['duration_ms']
        #convertendo milisegundos (dados pelo spotify) em minutos e segundos
        duration = int(duration)
        seconds=(duration/1000)%60
        seconds = int(seconds)
        minutes=(duration/(1000*60))%60
        minutes = int(minutes)

        duracao = ("%02d:%02d" % (minutes, seconds))
        lista_popularidade.append(duracao)
    return lista_popularidade

def pegar_duracao_musicas_banda(spotify_id_list: list):
    '''Usando os ids dos álbuns do spotify a função obtem a popularidade de todas as músicas
    dos álbuns dados e retorna um dataframe com esses valores de popularidade
    
	:param spotify_id_list: Lista de ids dos álbuns do spotify
	:spotify_id_list type: list
	:return: Dataframe da popularidade das músicas
	:rtype: DataFrame
    '''
    lista_duracoes = []

    for album in spotify_id_list:
        lista_duracoes += pegar_duracao_musicas_album_spotify(album)
    dados = {'Duração':lista_duracoes}
    df = pd.DataFrame(data=dados)
    return df

def pegar_popularidade_album_spotify(spotify_id: str):
    '''Usando o id de um álbum do spotify a função obtem a popularidade de todas as músicas
    desse álbum e retorna uma lista com esses valores de popularidade
    
	:param spotify_id: Ids do álbum do spotify
	:spotify_id type: str
	:return: Lista da popularidade das músicas
	:rtype: list
    '''
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='1a9faa80969a428cae902caf7caa6402', client_secret='d4ec70ec23114cd8a19b7b4dcf51aa62'))

    results = spotify.album_tracks(spotify_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results)

    lista_popularidade = []

    for track in tracks:
        track_id = track['id']
        track_page = spotify.track(track_id)
        popularity = track_page['popularity']
        lista_popularidade.append(popularity)
    return lista_popularidade

def pegar_popularidade_banda_spotify(spotify_id_list: list):
    '''Usando os ids dos álbuns do spotify a função obtem a popularidade de todas as músicas
    dos álbuns dados e retorna um dataframe com esses valores de popularidade
    
	:param spotify_id_list: Lista de ids dos álbuns do spotify
	:spotify_id_list type: list
	:return: Dataframe da popularidade das músicas
	:rtype: DataFrame
    '''
    lista_popularidade_banda = []
    for spotify_id in spotify_id_list:
        lista_popularidade_banda += pegar_popularidade_album_spotify(spotify_id)
    dados = {'Popularidade':lista_popularidade_banda}
    df = pd.DataFrame(data=dados)
    return df


def gerar_dataframe_album(url: str):
    '''Usando as funções criadas está função cria um dataframe de um álbum dado a partir de
    um url do site lyrics.com da página desse álbum
    
	:param url: Link da página do álbum
	:url type: str
	:return: Dataframe do álbum
	:rtype: DataFrame
    '''
    print('O processo pode demorar um pouco dependendo da quantidade de músicas. Aguarde...')
    #O conteúdo do dataframe é formado por ano, compositores, visualizações e letra, e seus índices são os títulos das músicas
    dados = {
        'Ano':pegar_ano_musicas_album(url),
        'Compositores':pegar_compositores_musicas_album(url),  
        'Letra':pegar_letras_musicas_album(url)}

    df = pd.DataFrame(data=dados, index=[pegar_titulos_musicas_album(url)])
    print(df)
    return df

def gerar_dataframe_banda(url_list: list):
    '''Usando as funções criadas e recebendo como parâmetro uma lista de links esta
    função obtem um dataframe de uma banda dada a partir de uma lista de urls com
    os seus álbums
    
	:param url_list: Lista de links dos albuns da banda
	:url_list type: list
	:return: Dataframe da banda
	:rtype: DataFrame
    '''

    lista_titulos = []
    lista_letras = []
    lista_anos = []
    lista_compositores = []
    lista_titulo_album = []

    for album in url_list:
        lista_titulos += pegar_titulos_musicas_album(album)
        lista_letras += pegar_letras_musicas_album(album)
        lista_anos += pegar_ano_musicas_album(album)
        lista_compositores += pegar_compositores_musicas_album(album)
        numero_faixas = len(pegar_letras_musicas_album(album))
        lista_titulo_album += [pegar_titulo_album(album)]*numero_faixas

    dados = {'Ano':lista_anos, 'compositores':lista_compositores, 'letra':lista_letras}
    indice = [lista_titulo_album, lista_titulos]
    df = pd.DataFrame(data=dados, index=indice)
    return df