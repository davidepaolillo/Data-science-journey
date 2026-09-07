# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:56:48 2022

@author: lilpao
"""


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
#
# _ 3.1 _ ANALISI ESPLORATIVA DEI DATI CON SEABORN
#

# Nella scorsa lezione abbiamo visto come fare grafici con matplotlib, possiamo però ottenere risultati ancora migliori 
# con il pacchetto seaborn insieme a quello di mpl

churn = pd.read_csv('churn_miss')
print(churn.head(30)) # prime 5 righe

# Con Seaborn possiamo, in questo modo, visualizzare un grafico ad es. di una variabile qualitativa come 'gender'
# Quindi specifichiamo la variabile da rappresentare e il dataset in questa maniera.

#sns.countplot(x= 'gender', data=churn)  # semplicemente conta i casi per una determinata variabile

# in questo caso utilizziamo barplot, per due variabili, specificando che vogliamo il genere e la cifra spesa nell'ultima transazione

#sns.barplot(x='gender',y='lasttrans',data=churn,palette='rainbow') # specifichiamo anche i colori con il
                                                                    # parametro palette
# penso sia la media 

#sns.boxplot(data=churn)   ## con il boxplot non specifico le variabili e mi dà le variabili numeriche ##

# Possiamo vedere l'andamento di una singola variabile in questa maniera
#sns.kdeplot(churn.age) #glielo dico in questa maniera

# Oppure posso fare il grafico a vagina
#sns.violinplot(data=churn)

# mentre la rappresentazione per scatterplot cioè per punti la si ottiene in questo modo
#sns.stripplot(x='label', y='age', data= churn, jitter=True # bello questo

#sns.stripplot(x='label', y='age', data= churn, hue='gender',jitter=True)
#questo ancora di più, perchè oltre a vedere che i giovani sono piu fedeli, vedo che le donne sono meno fedeli

#sns.stripplot(x='label', y='age', data= churn, hue='gender',split=True,jitter=True)
# Aggiungendo il parametro split mi visualizza le colonne separate

#sns.jointplot(x='age',y='lasttrans',data=churn,kind='scatter') grafico piu complesso e brutto


# Per visualizzare un analisi di regressione si può fare cosi:
#sns.lmplot(x='age', y='lasttrans',data=churn)

# Anche qui si puo differenziare in base al genere
#sns.lmplot(x='age', y='lasttrans',hue='gender',data=churn)

# se al posto di hue metto col ho due grafici, uno delle femmine e uno dei maschi

# Notiamo che il dataset contiene dei dati mancanti.
# Una delle cose che il pacchetto di seaborn ci permette di fare è creare una heatmap in cui visualizziamo 
# i dati mancanti.

#sns.heatmap(churn.isnull())  # vediamo che la maggior parte dei NaN è nella variabile label

# Vediamo le ultime cose ma prima carichiamo alcuni datasets inclusi in Seaborn

flights = sns.load_dataset('flights')
sns.heatmap(flights.corr(),annot = True) # In questo modo vediamo le correlazioni tra le variabili numeriche

f1 =flights.pivot_table(values='passengers',index='month',columns='year')  
sns.heatmap(f1)                                                              
# Vedo che i valori sono più concentrati a Luglio e Agosto


#sns.clustermap(f1,cmap='Accent')

iris=sns.load_dataset('iris')
sns.pairplot(iris)   # questo spacca perchè mostra grafici di tutte le variabili in un solo grafico.






