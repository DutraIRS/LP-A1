import scrape as sp

df = sp.gerar_dataframe_banda(['https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D', 
'https://www.lyrics.com/album/8760/G-N%27-R-Lies', 
'https://www.lyrics.com/album/2006860/Use-Your-Illusion-I', 
'https://www.lyrics.com/album/8762/Use-Your-Illusion-II', 
'https://www.lyrics.com/album/188450/The-Spaghetti-Incident%3F', 
'https://www.lyrics.com/album/1730175/Chinese-Democracy'])
df.to_csv('music.csv')

'''df = sp.gerar_dataframe_album('https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D')'''

#print(sp.pegar_visualizacoes('http://youtube.com/watch?v=1w7OgIMMRc4'))
#print(sp.pegar_link_youtube('https://www.lyrics.com/lyric/668824/Welcome+to+the+Jungle'))
#print(sp.pegar_visualizacoes_musicas_album('https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D'))

#print(sp.pegar_compositores('https://www.lyrics.com/lyric/35131103/Guns+N%27+Roses/Down+on+the+Farm'))
#print(sp.pegar_compositores_musicas_album('https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D'))