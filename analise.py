import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('movie.csv')

def changeValues(dataframe, column, intervals, targets):
  j=0
  for i in intervals:
    for key, value in dataframe[column].items():
      if value>=i[0] and value<i[1]:
        df.loc[key, column]=values_score[j]
    j+=1

intervals_score=[[0, 4], [4, 7.5], [7.5, 10]]
values_score=[1, 3, 5]

changeValues(df, 'score', intervals_score, values_score)

sns.scatterplot(data=df, x='votes', y='runtime', hue='rating', palette="RdPu", edgecolor='black', legend=True, size='score', linewidth=1.0, sizes=(10, 100))

plt.xlabel('Votes')
plt.ylabel('Runtime')

plt.show()