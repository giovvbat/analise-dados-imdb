import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('movie.csv')

# ranges para o 'score' e a proporção de tamanho entre as bolinhas
intervals_score=[[0, 4], [4, 7.5], [7.5, 10]]
values_score=[1, 3, 5]

# função auxiliar para tornar o tamanho dos pontos proporcional ao seu 'score', de acordo com as ranges definidas
def changeValues(dataframe, column, intervals, targets):
  j=0
  for i in intervals:
    for key, value in dataframe[column].items():
      if value>=i[0] and value<i[1]:
        df.loc[key, column]=values_score[j]
    j+=1

changeValues(df, 'score', intervals_score, values_score)

# projetando o gráfico e mudando o nome dos eixos
sns.scatterplot(data=df, x='votes', y='runtime', hue='rating', palette="RdPu", edgecolor='black', legend=True, size='score', linewidth=1.0, sizes=(10, 100))
plt.xlabel('Votes')
plt.ylabel('Runtime')

plt.show()