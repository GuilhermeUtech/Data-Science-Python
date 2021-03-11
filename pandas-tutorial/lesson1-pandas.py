# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)

from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)

import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
#print('Python version ' + sys.version)
#print('Pandas version ' + pd.__version__)
#print('Matplotlib version ' + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

#Como fazer um "merge" entre duas listas?
BabyDataSet = list(zip(names,births))

#Como criar um objeto dataframe?
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

print(df)

#Como escrever em um CSV utilizando Pandas?
df.to_csv('births1880.csv',index=False,header=False)

#E como ler um CSV?
#Location = r'C:\notebooks\pandas\births1880.csv'
#df = pd.read_csv(Location)

#E por fim, como excluir um CSV?
#import os
#os.remove(Location)

#Como checar todos os tipos das colunas?
df.dtypes

#Como checar o tipo de dados dessa coluna Births que meu dataset contém?
#print (df.Births.dtype)


# Analizar os dados, objetivo: encontrar o nome mais popular

Sorted = df.sort_values(['Births'], ascending=False)
#print(Sorted.head(1))


#ou

#print(df['Births'].max())

# Create graph
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), 
                   xytext=(25, 0), 
                   xycoords=('axes fraction', 'data'), 
                   textcoords='offset points',
                   arrowprops=dict(arrowstyle='-|>'))

#print("The most popular name")
df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used