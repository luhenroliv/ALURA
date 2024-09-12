#PYTHON_DATASCIENCE_ALURA

#NOTAS:
#Extração de dados analíticos do site: http://movielens.org, que apresenta dados e avaliações para
filmes. Arquivos da pasta "ml-latest-small" em formatos CSV.
#Após extração, a análise é realizada gerando importação em pandas (tanto cloud quanto na máquina),
para avaliar diferentes dados segmentados nos arquivos CSV.

#EXEMPLO IMPORTAÇÃO:
#Importação em pandas diretamente em cloud do arquivo "ratings".

import pandas as pd
    pd.read_csv("ratings.csv")

or

#Para avaliar as 5 primeiras linhas do arquivo, incluindo cabeçario.
import pandas as pd
notas = pd.read_csv("ratings.csv")
notas.head()

#QUANTIDADE DE AVALIAÇÕES:
import pandas as pd
notas = pd.read_csv("ratings.csv")
notas.head()
notas.shape
#(QTD DE AVALIACOES, QTD DE COLUNAS)


#VARIAÇÕES DE NOMES DAS COLUNAS, com dataframes pandas:
import pandas as pd
notas = pd.read_csv("ratings.csv")
notas.head()
notas.shape
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas.head ()


#ANÁLISE DE COLUNA ESPECÍFICA:
notas['nota']


#DATAFRAME SERIES PANDAS:
#Análise de valores distintos (UNIQUE)
import pandas as pd
notas = pd.read_csv("ratings.csv")
notas.head()
notas.shape
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas.head ()
notas['nota']
notas['nota'].unique()


#CONTAGEM DE VALORES POR NOTA:
import pandas as pd
notas = pd.read_csv("ratings.csv")
notas.head()
notas.shape
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas.head ()
notas['nota']
notas['nota'].unique()
notas['nota'].value_counts()


#MEDIA DE VALORES POR NOTA:
import pandas as pd
notas = pd.read_csv("ratings.csv")
notas.head()
notas.shape
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas.head ()
notas['nota']
notas['nota'].unique()
notas['nota'].value_counts()
notas['nota'].mean()


#02
##Other formats dataframe (pandas)
notas.nota.head() #5 firts line
notas.nota.plot() #create graphic disorganized
notas.nota.plot(kind='hist') #create graphic coherent
notas['nota'].median() #median number
notas.nota.describe() #descriptive statistics

#seaborn dataframe for gaphics and visualizations
#example:

import seaborn as
sns.boxplot(notas.nota)

#SUMMARY OF CONTENT:
#Import pandas (data analysis library)
#Read CSV data
#Upload file to Google Colab
#Rename columns
#Count data
#Improve data visualization





