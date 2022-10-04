import scrape as sp
import pandas as pd

#O site escolhido para a obtenção das letras e o site usado para verificar a popularidade e a duração das músicas têm divergências
#Há diferença de número de músicas e ordem das músicas no album, Obteremos então as letras, os compositores, o ano de lançamento
#e os títulos das músicas, usando a função 'gerar_dataframe_banda', salvaremos o Dataframe em um arquivo CSV e faremos a limpeza

df = sp.gerar_dataframe_banda([
'https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D',
'https://www.lyrics.com/album/8760/G-N%27-R-Lies',
'https://www.lyrics.com/album/2006860/Use-Your-Illusion-I', 
'https://www.lyrics.com/album/8762/Use-Your-Illusion-II', 
'https://www.lyrics.com/album/188450/The-Spaghetti-Incident%3F', 
'https://www.lyrics.com/album/1730175/Chinese-Democracy'])
df.to_csv('music_bruto.csv')

#Após a limpeza do dataframe anexaremos também a duração das músicas e sua popularidade
df1 = pd.read_csv(r'D:/Downloads/LP-A1/Código/Scrape/Dataframes/music_limpeza.csv')

#Duração das músicas dos álbuns da banda
df2 = sp.pegar_duracao_musicas_banda(['3I9Z1nDCL4E0cP62flcbI5','1RCAG3LrDwYsNU5ZiUJlWi','0CxPbTRARqKUYighiEY9Sz','00eiw4KOJZ7eC3NBEpmH4C','4ieR19hRkKeE81CalJPQNu','0suNLpB9xraAv1FcdlITjQ'])
#Popularidade de cada música dos álbuns da banda
df3 = sp.pegar_popularidade_banda_spotify(['3I9Z1nDCL4E0cP62flcbI5','1RCAG3LrDwYsNU5ZiUJlWi','0CxPbTRARqKUYighiEY9Sz','00eiw4KOJZ7eC3NBEpmH4C','4ieR19hRkKeE81CalJPQNu','0suNLpB9xraAv1FcdlITjQ'])

df = pd.concat([df1, df2, df3], axis=1, join='inner')
df = df.rename({'Unnamed: 0': 'Álbum', 'Unnamed: 1': 'Faixas'}, axis=1)
df = df.set_index(['Álbum', 'Faixas'], drop=True)
print(df)
df.to_csv(r'D:/Downloads/LP-A1/Código/Scrape/Dataframes/music.csv')