import os
import sys
import pandas as pd
import ntpath
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == "__main__":
    head, tail = ntpath.split(os.path.realpath(__file__))
    os.chdir(head)

    sys.path.insert(0, './Scrape')
    sys.path.insert(0, './Wordclouds')

    import scrape as sp
    import wordclouds as wcs

    music_df = pd.read_csv('Scrape/Dataframes/music.csv')

    print('Grupo de Perguntas 1:')

    print('\nMúsicas mais ouvidas e músicas menos ouvidas por Álbum\n')
    for album in music_df['Álbum'].unique():
        subdf = music_df[music_df['Álbum'] == album]
        sorted = subdf.sort_values(by='Popularidade', ascending=False)
        new_sorted = sorted.reset_index(drop=True)
        result = new_sorted[new_sorted.index < 3]
        print('As músicas mais ouvidas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
        sorted = subdf.sort_values(by='Popularidade', ascending=True)
        new_sorted = sorted.reset_index(drop=True)
        result = new_sorted[new_sorted.index < 3]
        print('As músicas menos ouvidas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n\n', '#'*42,'\n', sep='')
        
    print('Músicas mais longas e músicas mais curtas por Álbum\n')
    for album in music_df['Álbum'].unique():
        subdf = music_df[music_df['Álbum'] == album]
        sorted = subdf.sort_values(by='Duração', ascending=False)
        new_sorted = sorted.reset_index(drop=True)
        result = new_sorted[new_sorted.index < 3]
        print('As músicas mais longas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
        sorted = subdf.sort_values(by='Duração', ascending=True)
        new_sorted = sorted.reset_index(drop=True)
        result = new_sorted[new_sorted.index < 3]
        print('As músicas mais curtas do álbum ' + album + ' são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n\n', '#'*42,'\n', sep='')

    print('Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]\n')
    sorted = music_df.sort_values(by='Popularidade', ascending=False)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas mais ouvidas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
    sorted = music_df.sort_values(by='Popularidade', ascending=True)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas menos ouvidas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n\n', '#'*42,'\n', sep='')

    print('Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]\n')
    sorted = music_df.sort_values(by='Duração', ascending=False)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas mais longas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n', sep='')
    sorted = music_df.sort_values(by='Duração', ascending=True)
    new_sorted = sorted.reset_index(drop=True)
    result = new_sorted[new_sorted.index < 3]
    print('As músicas mais curtas da história da banda são:\n' + result['Faixas'][0] + ', ' + result['Faixas'][1] + ', ' + result['Faixas'][2] + '\n\n', '#'*42,'\n', sep='')

    print('Álbuns mais premiados [https://twiftnews.com/lifestyle/top-6-most-prestigious-music-awards/]\n')

    print('Existe alguma relação entre a duração da música e sua popularidade?\n')
    r2 = round(stats.pearsonr(music_df['Duração'], music_df['Popularidade'])[0] ** 2, 2)
    anotacao = 'R² = ' + str(r2)
    sns.scatterplot(music_df, y='Duração', x='Popularidade')
    plt.text(40, 600, anotacao, horizontalalignment='left', size='medium', color='black', weight='semibold')
    plt.savefig('../Figuras/Figura 3 - Gráfico de Dispersão Popularidade x Duração.png', dpi = 600)
    print('Conforme a Figura 3, o coeficiente de determinação é extremamente baixo. Logo, não exite correlação notável.\n\n', '#'*42, '\n', '#'*42, '\n', sep='')
    plt.clf()

    print('Grupo de Perguntas 2:')

    print('\nQuais são as palavras mais comuns nos títulos dos Álbuns?\n\n')
    titles_list = music_df['Álbum'].unique()
    dicio = {}
    for title in titles_list:
        for word in title.split(" "):
            val = dicio.get(word.lower(), 0)
            dicio[word.lower()] = val + 1

    words_list = []
    count_list = []

    for key in dicio:
        words_list.append(key)
        count_list.append(dicio[key])

    df_words = pd.DataFrame((words_list, count_list)).T
    df_words.rename(columns={0: "Words", 1: "Count"}, inplace = True)

    mask = df_words['Count'] == df_words['Count'].max()
    df_common_words = df_words[mask]

    print('A(s) palavra(s) mais comum(ns) nos títulos dos álbuns é(são):')
    for ind in range(len(df_common_words.index)):
        print(df_common_words['Words'].iloc[ind])

    print('Repetindo-se ' + str(df_common_words['Count'].iloc[0]) + ' vezes.\n\n', '#'*42, '\n', sep='')

    print('Quais são as palavras mais comuns nos títulos das músicas?\n')
    track_list = music_df['Faixas'].unique()

    dicio = {}

    for track in track_list:
        for word in track.split(" "):
            val = dicio.get(word.lower(), 0)
            dicio[word.lower()] = val + 1

    words_list = []
    count_list = []

    for key in dicio:
        words_list.append(key)
        count_list.append(dicio[key])

    df_words = pd.DataFrame((words_list, count_list)).T
    df_words.rename(columns={0: "Words", 1: "Count"}, inplace = True)

    mask = df_words['Count'] > df_words['Count'].max() - 8
    df_common_words = df_words[mask].sort_values(by='Count', ascending=False)

    print('A(s) palavra(s) mais comum(ns) nos títulos das faixas é(são):')
    for ind in range(len(df_common_words.index)):
        print(df_common_words['Words'].iloc[ind], ', repetindo-se ' + str(df_common_words['Count'].iloc[ind]) + ' vezes.', sep='')

    print('\nRemovendo as palavras triviais:')
    for ind in range(len(df_common_words.index)):
        if df_common_words['Words'].iloc[ind] not in 'a|the|an|the|to|in|for|of|or|by|with|is|on|that|be':
            print(df_common_words['Words'].iloc[ind], ', repetindo-se ' + str(df_common_words['Count'].iloc[ind]) + ' vezes.', sep='')

    print('\n', '#'*42, '\n', sep='')

    print('Quais são as palavras mais comuns nas letras das músicas, por Álbum?\n')

    print('Quais são as palavras mais comuns nas letras das músicas, em toda a discografia?\n')

    print('\n', '#'*42, '\n', sep='')

    print('O título de um álbum é tema recorrente nas letras?\n')

    print('\n', '#'*42, '\n', sep='')

    print('O título de uma música é tema recorrente nas letras?\n')

    print('\n', '#'*42, '\n', '#'*42, '\n', sep='')

    print('Grupo de Perguntas 3:\n')

    print('Compositor (não integrante da banda) mais comum;\n')

    print('\n', '#'*42, '\n', sep='')

    print('Música mais popular por compositor;\n')

    print('\n', '#'*42, '\n', sep='')

    print('Ano em que a banda recebeu mais prêmios.\n')

    print('\n', '#'*42, '\n', '#'*42, '\n', sep='')

    print('Visualizações')

    print('Confira as Figura 4A a 4F')

    print('\n', '#'*42, '\n', sep='')

    print('Confira as Figura 5A a 5F')

    print('\n', '#'*42, '\n', sep='')

    sorted = music_df.sort_values(by='Popularidade', ascending=False)
    sns.barplot(sorted, x='Popularidade', y='Faixas')
    plt.savefig('../Figuras/Figura 6 - Gráfico de Barras da Popularidade', dpi = 600)
    plt.clf()

    print('Confira a Figura 6')

    print('\n', '#'*42, '\n', sep='')

    sorted = music_df.sort_values(by='Duração', ascending=False)
    sns.barplot(sorted, x='Duração', y='Faixas')
    plt.savefig('../Figuras/Figura 7 - Gráfico de Barras da Duração', dpi = 600)
    plt.clf()

    print('Confira a Figura 7')

    print('\n', '#'*42, '\n', sep='')

    print('Confira a Figura 8')

    print('\n', '#'*42, '\n', sep='')

    print('Confira a Figura 3')

    print('\n', '#'*42, '\n', sep='')

    ignore = "a|the|an|the|to|in|for|of|or|by|with|is|on|that|be|but|you|your|i|it|i'm|it's|and|when|i've|where|to|an|i'd|from"
    texto_titulos_alb = ''
    for titulo_alb in range(len(music_df['Álbum'])):
        location = titulo_alb - 1
        texto_titulos_alb = texto_titulos_alb + ' ' + music_df['Álbum'].iloc[location]

    dic_freq = wcs.criar_dic_freq(texto_titulos_alb, ignore)
    wcs.criar_imagem("../Figuras/guns_mask.png", dic_freq, '../Figuras/Figura 9 - Tag Cloud da Pergunta 2 (i)')
    plt.clf()

    print('Confira a Figura 9')

    print('\n', '#'*42, '\n', sep='')

    texto_titulos_mus = ''
    for titulo_mus in range(len(music_df['Faixas'])):
        location = titulo_mus - 1
        texto_titulos_mus = texto_titulos_mus + ' ' + music_df['Faixas'].iloc[location]

    dic_freq = wcs.criar_dic_freq(texto_titulos_mus, ignore)
    wcs.criar_imagem("../Figuras/guns_mask.png", dic_freq, '../Figuras/Figura 10 - Tag Cloud da Pergunta 2 (ii)')
    plt.clf()

    print('Confira a Figura 10')

    print('\n', '#'*42, '\n', sep='')

    texto_letras = ''
    for letra in range(len(music_df['letra'])):
        location = letra - 1
        texto_letras = texto_letras + ' ' + music_df['letra'].iloc[location]

    dic_freq = wcs.criar_dic_freq(texto_letras, ignore)
    wcs.criar_imagem("../Figuras/guns_mask.png", dic_freq, '../Figuras/Figura 11 - Tag Cloud da Pergunta 2 (iv)')
    plt.clf()

    print('Confira a Figura 11')

    print('\n', '#'*42, '\n', '#'*42, '\n', sep='')

    print('Muito obrigado pela sua atenção! :)')