import scrape as sp
'''
df = sp.gerar_dataframe_banda(['https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D', 
'https://www.lyrics.com/album/8760/G-N%27-R-Lies', 
'https://www.lyrics.com/album/2006860/Use-Your-Illusion-I', 
'https://www.lyrics.com/album/8762/Use-Your-Illusion-II', 
'https://www.lyrics.com/album/188450/The-Spaghetti-Incident%3F', 
'https://www.lyrics.com/album/1730175/Chinese-Democracy'])
'''
df = sp.gerar_dataframe_album('https://www.lyrics.com/album/8763/Appetite-for-Destruction-%5BEdited%5D')

df.to_csv('csvguns.csv')