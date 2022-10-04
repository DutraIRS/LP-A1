import scrape as sp
import os 
import pandas as pd

#O site escolhido para a obtenção das letras e o site usado para verificar a popularidade e a duração das músicas têm divergências
#Há diferença de número de músicas e ordem das músicas no album, Obteremos então as letras, os compositores, o ano de lançamento
#e os títulos das músicas, usando a função 'gerar_dataframe_banda', salvaremos o Dataframe em um arquivo CSV e faremos a limpeza

'''df = sp.gerar_dataframe_banda([
'https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D',
'https://www.lyrics.com/album/8760/G-N%27-R-Lies',
'https://www.lyrics.com/album/2006860/Use-Your-Illusion-I', 
'https://www.lyrics.com/album/8762/Use-Your-Illusion-II', 
'https://www.lyrics.com/album/188450/The-Spaghetti-Incident%3F', 
'https://www.lyrics.com/album/1730175/Chinese-Democracy'])
df.to_csv('music_bruto.csv')'''

#Após a limpeza do dataframe anexaremos também a duração das músicas e sua popularidade
df = pd.read_csv(r'/Dataframes/music.csv')
print(df)
#df1 = pd.read_csv(r'/Dataframe/data.csv')
#df2 = sp.pegar_duracao_musicas_banda(['3I9Z1nDCL4E0cP62flcbI5','1RCAG3LrDwYsNU5ZiUJlWi','0CxPbTRARqKUYighiEY9Sz','00eiw4KOJZ7eC3NBEpmH4C','4ieR19hRkKeE81CalJPQNu','0suNLpB9xraAv1FcdlITjQ'])

'''df2 = sp.pegar_duracao_musicas_banda([
    'https://pt.wikipedia.org/wiki/Appetite_for_Destruction',
    'https://pt.wikipedia.org/wiki/G_N%27_R_Lies',
    'https://pt.wikipedia.org/wiki/Use_Your_Illusion_I',
    'https://pt.wikipedia.org/wiki/Use_Your_Illusion_II',
    'https://pt.wikipedia.org/wiki/The_Spaghetti_Incident%3F',
    'https://pt.wikipedia.org/wiki/Chinese_Democracy'])

df = pd.read_csv(r'D:\Downloads\LP-A1\A1\music_semduracao.csv')

df3 = pd.concat([df, df2], axis=1, join='inner')
df3 = df3.set_index(['Unnamed: 0', 'Unnamed: 1'])
df3.to_csv('music.csv')'''

#print(sp.pegar_popularidade_album_spotify('3I9Z1nDCL4E0cP62flcbI5'))
#print(len(sp.pegar_popularidade_banda_spotify(['3I9Z1nDCL4E0cP62flcbI5','1RCAG3LrDwYsNU5ZiUJlWi','0CxPbTRARqKUYighiEY9Sz','00eiw4KOJZ7eC3NBEpmH4C','4ieR19hRkKeE81CalJPQNu','0suNLpB9xraAv1FcdlITjQ'])))

#print(sp.pegar_visualizacoes('http://youtube.com/watch?v=1w7OgIMMRc4'))
#print(sp.pegar_link_youtube('https://www.lyrics.com/lyric/668824/Welcome+to+the+Jungle'))
#print(sp.pegar_visualizacoes_musicas_album('https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D'))

#print(sp.pegar_compositores('https://www.lyrics.com/lyric/35131103/Guns+N%27+Roses/Down+on+the+Farm'))
#print(sp.pegar_compositores_musicas_album('https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D'))