#PYTHON_DATASCIENCE_ALURA
#working table movies

#IN CLOUD: table filmes
import pandas as pd
filmes = pd.read_csv("movies.csv")
filmes.head()

#See Toy Story movie notes
import pandas as pd
filmes = pd.read_csv("movies.csv")
filmes.columns = ["filmeid", "titulo", "generos"]
filmes.head()

#Analyzing some specific notes per film
notas.head()
notas.query("filmeid==1").nota.mean()

#movie and mean (note movie for mean)
notas.groupby("filme-d").mean()["nota"]

#graphic
medias_por_filme.plot(kind='hist')

sns.boxplot(medias_por_filme) #graphic
medias_por_filme.describe()

#distribution graph
sns.distplot(medias_por_filme)

#more dataframe graphics

import matplotlib.pyplot as plt
plt.hist(medias_por_filme)
plt.title("Histograma das medias dos filmes")
sns.boxplot(y=medias_por_filme)

#02
import matplotlib.pyplot as plt
plt.figure(figsize=(5,8))
sns.boxplot(y=medias_por_filme)

#Summary:
#Work with query;
#Identify the bins; and
#Filter only one column.



