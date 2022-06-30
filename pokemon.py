"""
Created on Wed Jun 15 16:05:18 2022

@author: Wm. Lenord Stage
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv('pokemon.csv')

#print(df.head(5))

def clean_names(Name):
    return Name.split(' ')[0]
df['Clean Names'] = df['Name'].apply(lambda x: clean_names(x))

count_by_type1 = df.groupby('Type 1').count()
count_by_type1.to_csv('count_by_typea.csv')
count_by_type1a = pd.read_csv('count_by_typea.csv')

count_legendary = df.groupby('Legendary').count()
#print(count_legendary)
count_legendary.to_csv('count_legendary.csv')
count_legendary2 = pd.read_csv('count_legendary.csv')
av= sns.barplot(data=count_legendary2, x ='Clean Names', y='Legendary')
sns.set_palette("pastel")
sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
plt.ylabel('Legendary')
plt.xlabel('Number of Clean Names')
plt.title('Number of Legendary')
plt.rcParams['figure.figsize'] = [10, 10]
plt.show()
#plt.savefig('Number of Legendary.png')

#print(count_by_type1a)
ar= sns.barplot(data=count_by_type1a, x ='Clean Names', y='Type 1')
sns.set_palette("pastel")
sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
plt.ylabel('Type 1')
plt.xlabel('Number ')
plt.title('Number of Type 1-Grouped')
plt.rcParams['figure.figsize'] = [10, 10]
plt.show()
#plt.savefig('Number of Type 1-Grouped.png')

count_by_type2 = df.groupby('Type 2').count()
count_by_type2.to_csv('count_by_typeb.csv')
count_by_type1b = pd.read_csv('count_by_typeb.csv')

#print(count_by_type1b)
aq= sns.barplot(data=count_by_type1b, x ='Clean Names', y='Type 2')
sns.set_palette("pastel")
sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
plt.ylabel('Type 2')
plt.xlabel('Number ')
plt.title('Number of Type 2-Grouped')
plt.rcParams['figure.figsize'] = [10, 10]
plt.show()
#plt.savefig('Number of Type 2-Grouped.png')
#print(df.dtypes)
df2 = df
count_by_speedd = df2.sort_values('Speed', ascending=False).head(25)[['Speed', 'Clean Names']]

at= sns.barplot(data=count_by_speedd, x='Speed', y='Clean Names', ci=None)
sns.set_palette("pastel")
sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
plt.ylabel('Name')
plt.xlabel('Speed')
plt.title('Top 15 by Speed')
plt.rcParams['figure.figsize'] = [10, 10]
plt.show()
#plt.savefig('Top 15 by Speed.png')

count_legendary_names = df.sort_values('Legendary', ascending=False).head(65)[['Legendary', 'Clean Names']]
count_legendary_names_alpha = count_legendary_names.sort_values('Clean Names')
count_legendary_names_alpha['CleanNames'] = count_legendary_names_alpha['Clean Names']
count_legendary_names_alpha1 = count_legendary_names_alpha.iloc[:32]
count_legendary_names_alpha2 = count_legendary_names_alpha.iloc[33:]

text = " ".join(i for i in count_legendary_names_alpha1.CleanNames)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="black").generate(text)
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Legendary 1')
plt.axis("off")
plt.show()
#plt.savefig('Legendary 1.png')

text = " ".join(i for i in count_legendary_names_alpha2.CleanNames)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Legendary 2')
plt.axis("off")
plt.show()
#plt.savefig('Legendary 2.png')

#print(count_legendary_names_alpha)


df3=df
df3['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df4 = df
df4['Total'] = df.iloc[:, 4:10 ].sum(axis=1)
df4 = df4[['#', 'Clean Names', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total', 'Generation', 'Legendary']]


totals = df4.sort_values('Total', ascending=False).head(30)[['Total', 'Clean Names']]
ax= sns.barplot(data=totals, x='Total', y='Clean Names')
sns.set_palette("pastel")
sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
plt.ylabel('Name')
plt.xlabel('Points Total')
plt.title('Top 30 by Total Points')
plt.rcParams['figure.figsize'] = [10, 10]
plt.show()
#plt.savefig('Top 30 by Total Points.png')

totalsx = df4.sort_values('Total', ascending=False).head(60)[['Total', 'Clean Names']]
totalsgb = totalsx.groupby('Total').sum().reset_index()

ay= sns.barplot(data=totalsgb, x='Total', y='Clean Names')
sns.set_palette("pastel")
sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
plt.ylabel('Names')
plt.xlabel('Points Total')
plt.title('Top 60 by Total Points')
plt.rcParams['figure.figsize'] = [12, 10]
plt.show()
#plt.savefig('Top 60 by Total Points.png')
totalsy = df4.groupby('Total').count()
sns.displot(totalsy['Clean Names'], kde=True)
plt.rcParams['figure.figsize'] = [10, 10]
plt.style.use('fivethirtyeight')
plt.title ("Distribution of Total Points")
plt.xlabel('Number of Pokemon')
plt.ylabel('Count of Pokemon Grouped by Point Total')
sns.set_palette("pastel")
#plt.savefig('Distribution of Total Points.png')
plt.show()


    

  