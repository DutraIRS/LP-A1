import matplotlib.pyplot as plt
import wordcloud as wc
import numpy as np
import PIL
import re
import os
import ntpath

head, tail = ntpath.split(os.path.realpath(__file__))
os.chdir(head)

def criar_dic_freq(text: str, ignore: str):
    '''
    A função recebe uma string com o texto a ser avaliado e, para cada palavra no texto,
    testa se ela está na lista de palavras a serem desconsideradas. Caso não esteja, procura
    seu valor em um dicionário, atribuindo valor zero se não for encontrada no dicionário.
    Por fim, 1 é adicionado ao valor, que representa a frequência absoluta da palavra no arquivo.

    :param text: Texto-base para o WordCloud
    :text type: str
    :param ignore: Palavras a ignorar formatadas de maneira adequada para regex
    :ignore type: str
    :return: Dicionário de cada palavra (fora as previamente excluídas) e suas contagens
    :r type: dict
    '''

    dic = {}

    for word in text.split(" "):
        if re.match(ignore, word):
            continue

        val = dic.get(word.lower(), 0)
        dic[word.lower()] = val + 1

    return dic

def criar_imagem(mask, dic, name):
    '''
    Recebe uma imagem máscara, um dicionário de frequências e um nome para o output.
    Traduz a máscara para um array NumPy, gera a WordCloud com até 1000 palavras mais frequentes.
    Traduz a imagem de volta para array para transformar todas as cores (além do branco) em preto.
    Gera a figura com o matplotlib.

    :param mask: Nome do arquivo que será a imagem máscara
    :mask type: str
    :param dic: Dicionário de frequências das palavras
    :dic type: dict
    :param name: Nome do arquivo que será gerado
    :name type: str
    '''
    cloud_mask = np.array(PIL.Image.open(mask))

    cloud = wc.WordCloud(background_color="white", max_words=100, mask=cloud_mask)
    cloud = cloud.generate_from_frequencies(dic)

    fig = np.array(cloud)
    fig[fig != 255] = 0

    plt.imshow(fig, interpolation="nearest")
    plt.axis("off")
    plt.savefig(name + '.png', dpi=600)

####################################

#dic_freq = criar_dic_freq('guns.txt', "a|the|an|the|to|in|for|of|or|by|with|is|on|that|be")
#criar_imagem("../../Figuras/guns_mask.png", dic_freq, '../../Figuras/guns')