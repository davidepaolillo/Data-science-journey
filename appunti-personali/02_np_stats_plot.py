# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:11:33 2022

@author: lilpao
"""

# In precedenza abbiamo visto come con l'aiuto di un seed e dei pacchetti pandas e numpy
# possiamo estrarre sempre gli stessi casoi da un dato dataset

# Numpy comprende anche una serie di funzioni utili per generare dei dataset casuali

#
# _ 2.1 _ CREARE DEI DATASET CASUALI 
#

import pandas as pd
import numpy as np
# Usiamo la funzione DataFrame di pandas (già vista) ma gli passiamo all'interno una funzione di numpy che genera dati casuali
df1=pd.DataFrame(np.random.randn(10,5))      # in cui specifichiamo il numero di casi (10) ovvero righe                                             # e il numero di variabili (5) del nostro dataframe che vogliamo creare
print(df1)

# Ovviamente ripetendo questo codice otterremmo sempre risultati diversi a meno di impostare un seed.
np.random.seed(12345)  # Basta mettere sempre lo stesso numero tra parentesi e si ottiene sempre lo stesso risultato
pd.DataFrame(np.random.randn(5,3))
# Eseguendo più volte questo blocco di codice otterremo sempre lo stesso risultato in output

# Le funzioni del pacchetto Numpy ci permettono di ottenere anche altri tipi di distribuzione (v.a)

# BINOMIALE
print('\n Distribuzione Binomiale \n')

print(pd.DataFrame(np.random.binomial(100,0.5,(10,5))))  # dove il primo parametro sono lr prove ripetute (es. lancio di una moneta) e il secondo la probabilità di successo

#POISSON
print('\n Distribuzione di Poisson \n')               # Dobbiamo anche sempre specificare la coppia casi,variabili

print(pd.DataFrame(np.random.poisson(5,(10,5))))  # dove il primo parametro è la media della Poisson (vedi wikipedia)

# UNIFORME
print('\n Distribuzione Uniforme \n')

print(pd.DataFrame(np.random.uniform(1,100,(8,4))))  # 1,100 sono gli estremi dell'intervallo chiuso [a,b]

# la distribuzione uniforme è una distribuzione di probabilità continua che è uniforme su un insieme, 
# ovvero che attribuisce la stessa probabilità a tutti i punti appartenenti ad un dato intervallo [a,b]
# contenuto nell'insieme.

## N.B. Come sempre possiamo ottenere informazioni per ognuna di queste funzioni 
## scrivendo sulla console la funzione e premendo Shift + Tab

#
# _ 2.2 _ STATISTICA DI BASE
#

#Consideriamo il solito Dataframe creato nella lezione (1)

df=pd.DataFrame({'Names': ['Lillo','Cucci','Iron','Renè','Laura','Simon','Laura'],
                  'Height':[176,170,80,38,160,180,160],'Weight':[70,34.5,60,14,57,75,57],
                  'Pref_Food':['Pizza del Paolo','Pasta al forno','Carne','Mango','Crispy mcBacon','Carbonara','Crispy mcBacon'],'Sex':['m','f','m','m','f','m','f']})



# Abbiamo già visto ad esempio la funzione describe()
# Possiamo utilizzarla insieme alla funzione transpose per ottenere semplicemente qualocsa di più leggibile
print(df.describe().transpose())

print('\n count, median, mean, ecc... \n')
# Possiamo verificare il conteggio dei valori in questo modo (vedere quindi se non ci sono missing values)
print(df.count())
# Oppure possiamo ottenere dei dati su variabili specifiche come ad esempio la mediana, la media, la deviazione std.
# e i valori minimi e massimi che già sappiamo di potere ottenere con la funzione .describe()

print('\n Mediana  ')
print(df['Height'].median())

print('\n Media')
print(df['Height'].mean())

print('\n Valore minimo')     # .max è speculare
print(df['Height'].min())

print('\n Deviazione Standard')      
print(df['Height'].std())

print('\n Indice Skew')
print(df['Height'].skew())

print('\n Indice di Kurt')
print(df['Height'].kurt())

print('\n Moda')
print(df['Height'].mode())

#
# _ 2.3 _ CREARE GRAFICI CON MATPLOTLIB
#


import matplotlib as mpl
import matplotlib.pyplot as plt

#plt.plot([5,7,2,4],[4,6,9,2],'ro') # prende in input due liste, inserendo il parametro 'ro' (round object) otterremo dei pallini rossi


x=[50,70,90,65]       # se runno i plot tutti assieme mi vengono sminchiati
y=[129,192,163,175]

#plt.plot(x,y,linewidth=4.0) # linewidth è lo spessore della linea
#plt.show()
#plt.plot(x,y,linewidth=1.0,marker='o',markersize=10,markerfacecolor='white')
# Abbiamo inserito dei marker dove ci sono i nostri dati


#come sempre possiamo visualizzare con help(plp.pyplot) la documentazione relativa alla nostra funzione (su jupyter è shift+tab)



## TITOLO E NOMI AGLI ASSI ##

"""plt.plot(x,y,color='yellow')
plt.title('TITOLO')
plt.xlabel('asse x')
plt.ylabel('asse y')
plt.grid(True)   # parametro aggiuntivo per avere la griglia
plt.legend('Legend')  # comando per inserire la legenda

plt.show()"""

## CREARE DEI SOTTOGRAFICI ##








## GRAFICI A TORTA ##  



#plt.pie(x)
#plt.show()

# possiamo creare una lista di colori e applicarla al parametro colors per modificare i colori del piechart
#colori=['red','green','purple','yellow']
#labels=['A','B','C','D'] # possiamo creare dei labels per etichettare le fette
#plt.pie(x,colors=colori,labels=labels)



## SCATTERPLOT ##

#plt.scatter(x,y)
#plt.show()

## ISTOGRAMMA ##

#plt.bar(x,y)
#plt.show()

""" Creiamo ora un dataframe casuali """

df2=pd.DataFrame(np.random.rand(10, 4), columns={'var1', 'var2', 'var3', 'var4'})
print('\n df2 \n')
print(df2)

#df2.plot(kind='bar')


## possiamo creare anche barre staked inserendo l'ooportuno parametro 

#df2.plot(kind='bar',stacked=True)

# Dal momento che abbiamo 4 variabili possiamo creare 4 istogrammi con la funzione hist
#df2.hist()
# Oppure per una sola variabile
#df2['var1'].hist()


## GRAFICO AREOLARE ##
#df2.plot(kind='area',stacked=False)


# salvare l'immagine nella working director ---> per salvarla bisogna togliere il comando plt.show()
plt.savefig('figura1.png')
# con il parametro aggiuntivo bpi si può modificare la grandezza dell'immagine


## STILI PER MODIFICARE UN GRAFICO ##

print('\n stili per modificare un grafico')
print(plt.style.available)

# Per applicare uni stile diverso lo scriviamo nella riga prima
#plt.style.use('classic')
#df2.plot(kind='area')



# Creiamo ancora due oggetti casuali con numpy e li rappresentiamo graficamente
df_1=np.random.randn(100)
df_2=np.random.randn(100)
print(df_1)
#plt.hist(df_1)

# Confrontiamo ora i due grafici

plt.hist(df_1, color='red', alpha=0.3, bins= 15)  # il rosso col blu fa il violaaaa 
plt.hist(df_2,color='blue', alpha=0.4, bins= 15)









 