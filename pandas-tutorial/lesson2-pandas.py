# Nessa segunda aula vamos começar a criar o nosso próprio conjunto de dados para analisar. Isso evita que o usuário final que esteja lendo este tutorial tenha que baixar quaisquer arquivos para replicar os resultados abaixo.
# Exportaremos esse conjunto de dados para um arquivo de texto para que você possa obter alguma experiência na extração de dados de um arquivo de texto.
# Import all libraries needed for the tutorial

import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys # only needed to determine Python version number
import matplotlib # only needed to determine Matplotlib version number

#print('Python version ' + sys.version)
#print('Pandas version ' + pd.__version__)
#print('Matplotlib version ' + matplotlib.__version__)
# The inital set of baby names

names = ['Bob','Jessica','Mary','John','Mel'] #nomes que vou criar randomicamente o dataSet
random.seed(500) # Não entendi mt o seed
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)] # sorteando 1000 nomes pra criar o data random_names
#  print(random_names[:10])

births = [random.randint(low=0,high=1000) for i in range(1000)] #sorteando a data de nascimento
#  print(births[:10])

DataSetBaby_Name = zip(random_names, births)
df = pd.DataFrame(data = DataSetBaby_Name, columns=['Names', 'Births']) #crio o data set e aplico os labels Names e Births
# print(df)

#Exportar esse data para um txt

df.to_csv('births1880.txt',index=False,header=False)

#Agora o inverso, importar esse data de um txt

Location = r'births1880.txt'
#df = pd.read_csv(Location)

# print(df.info()) #caraca que dahora, dá até o quanto de memória tá usando

#print(df.head()) # note aqui que quando eu puxo dados de um txt o header do dataSet é o primeiro registro, será arrumado abaixo
df = pd.read_csv(Location, header=None)

#  print(df.head())#O header arrumou utilizando o header=None, aproveitando: O .head() traz a "cabeça" do dataSet
#  print(df.tail()) #O tail traz o "rabo" do dataSet

#Mas como ao ler de um arquivo externo eu adicionar meus próprios HEADERS?

df = pd.read_csv(Location, names=["Nomes", "Nascimento"])

#  print(df.head())

# PREPARANDO DATA, VAMOS LIMPAR AS CONSULTAS QUE NÃO SEJAM ÚNICAS. Como? Através do unique()
#  print(df['Nomes'].unique())
#Existe uma outra forma de se fazer isso, através do groupby

name = df.groupby('Nomes')
df = name.sum()
#  print(df)

##  Analisando os Dados  ##

Sorted = df.sort_values(['Nascimento'], ascending=False)

# dois métodos diferentes para a mesma coisa

print(Sorted.head(1))
print(df['Nascimento'].max())

##   Apresentando os Dados   ##

# Criando gráficos

df['Nascimento'].plot.bar()
print("The most popular name")
df.sort_values(by='Nascimento', ascending=False)

##Cria um gráfico de barra com os nomes e o total dos valores##
