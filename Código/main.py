import os
import sys
import pandas as pd
import ntpath
import seaborn as sns
import matplotlib.pyplot as plt

head, tail = ntpath.split(os.path.realpath(__file__))
os.chdir(head)

sys.path.insert(0, './Scrape')
sys.path.insert(0, './Wordclouds')

import scrape as sp
import wordclouds as wc

head, tail = ntpath.split(os.path.realpath(__file__))
os.chdir(head)

music_df = pd.read_csv('Scrape/Dataframes/music.csv')

print('Grupo de Perguntas 1:')

print('Músicas mais ouvidas e músicas menos ouvidas por Álbum')
for album in music_df['Álbum'].unique():
    subdf = music_df[music_df['Álbum'] == album]
    sorted = subdf.sort_values(by='Popularidade', ascending=False)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas mais ouvidas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
    sorted = subdf.sort_values(by='Popularidade', ascending=True)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas menos ouvidas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n\n', sep='')
    
print('Músicas mais longas e músicas mais curtas por Álbum')
for album in music_df['Álbum'].unique():
    subdf = music_df[music_df['Álbum'] == album]
    sorted = subdf.sort_values(by='Duração', ascending=False)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas mais longas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
    sorted = subdf.sort_values(by='Duração', ascending=True)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas mais curtas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n\n', sep='')

print('Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]')
sorted = music_df.sort_values(by='Popularidade', ascending=False)
new_sorted = sorted.reset_index(drop=True)
result = new_sorted[new_sorted.index < 3]
print('As músicas mais ouvidas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
sorted = music_df.sort_values(by='Popularidade', ascending=True)
new_sorted = sorted.reset_index(drop=True)
result = new_sorted[new_sorted.index < 3]
print('As músicas menos ouvidas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')

print('Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]')
sorted = music_df.sort_values(by='Duração', ascending=False)
new_sorted = sorted.reset_index(drop=True)
result = new_sorted[new_sorted.index < 3]
print('As músicas mais longas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
sorted = music_df.sort_values(by='Duração', ascending=True)
new_sorted = sorted.reset_index(drop=True)
result = new_sorted[new_sorted.index < 3]
print('As músicas mais curtas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')

#Álbuns mais premiados [https://twiftnews.com/lifestyle/top-6-most-prestigious-music-awards/]
#Existe alguma relação entre a duração da música e sua popularidade?


print('Grupo de Perguntas 2:')

#print('Quais são as palavras mais comuns nos títulos dos Álbuns?')
#titles_list = music_df['Álbum'].unique()
#dicio = {}
#for title in titles_list:
#    for word in title.split(" "):
#        val = dicio.get(word.lower(), 0)
#        dicio[word.lower()] = val + 1
#dicio.values()

#Quais são as palavras mais comuns nos títulos das músicas?
#Quais são as palavras mais comuns nas letras das músicas, por Álbum?
#Quais são as palavras mais comuns nas letras das músicas, em toda a discografia?
#O título de um álbum é tema recorrente nas letras?
#O título de uma música é tema recorrente nas letras?


#Grupo de Perguntas 3:

#Compositor (não integrante da banda) mais comum;
#Música mais popular por compositor;
#Ano em que a banda recebeu mais prêmios.
sns.scatterplot(music_df[music_df['Álbum'] == 'Appetite for Destruction'], y='Duração', x='Popularidade')
plt.show()