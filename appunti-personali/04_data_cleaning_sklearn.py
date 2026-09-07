# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 00:17:50 2022

@author: lilpao
"""

#
# _ 4.1 _ PREPARAZIONE DEI DATI PER L'ANALISI
#

## DATA CLEANING ##

# I problemi possono essere ad esempio : molteplici diciture ( es. female, f , ff, fem per una variabile gender)
# Dati outlier (si discostano tropo dagli altri su quella colonna), o missing values

# Vediamo come trattare e gestire i missing values con Pandas

import pandas as pd
df_missing=pd.read_csv('df_missing.csv')
print(df_missing)  # abbiamo dati mancanti nelle variabili D,C e B

# Possiamo trattare i missing values tramite deletion o imputation (sostituzione con ad es. media)

print('\n deletion \n')

print(df_missing.dropna()) # per effettuare cancellazione delle righe con dati mancanti
print(df_missing.dropna(axis=1, how='any')) # possiamo anche (così) cancellare le colonne che contengonio i missing values

print('\n imputation \n')

# Come imputation possiamo ad esempio imputare il valore 0 semplicemente così

print(df_missing.fillna(0))

# Oppure possiamo metterci la media di quella variabile

print(df_missing.fillna(df_missing.mean()))


# PER IMPUTARE I DATI CON SCICKIT LEARN ci serviremo di un modulo apposito che andiamo ad importare

from sklearn import preprocessing
#from sklearn.preprocessing import Imputer   ## Non mi importa Imputer ...

# Andiamo a creare quindi, l'imputatore
#imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
# gli sto dicendo come identificare i missing values, che tipo di strategia voglio usare, e che ragioniamo per righe (0)

# adesso dobbiamo impostare l'imputatore in modo che funzioni sulle colonne che contengono i m.v. ovvero le colonne B, C, D

#imp = imp.fit(df_missing.iloc[:,1:4]) # 1:4 perchè sono le colonne B, C, D. Le righe le prendo tutte

# vedi il metodo .iloc in DATA_SCIENCE (1)

#df_missing.ilooc[:,1:4]=imp.trasform(df_missing.iloc[:,1:4])
#print(df_missing)


#
# _4.2_ ESEMPIO DI PULIZIA DI UN DATASET
#
print('\n esempio di pulizia di un Dataset \n')
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('students2.csv')
print(df)

print('\n')

#per prima cosa usiamo .dtypes per vedere che tipo di variabili abbiamo
print(df.dtypes)

print('\n')
# Prendiamo in considerazione una singola variabile (non numerica) e vediamo in quanti modi è stata codificata
print(df['gender'].value_counts())
print('\n')

# Se facciamo così:
print(df['mark1'].value_counts(dropna=False))  # Visualizziamo anche il numero dei missing values
print('\n')

print(df_missing.dropna().shape)

# Per visualizzare gli outliers invece, possiamo fare un .boxplot(), che mi fa un plot delle colonne con variabili numeriche

#df.boxplot( ) # vediamo che abbiamo 2 outliers, uno nella colonna mark1 e l'altro nella colonna mark2

# Per sistemarli basta usare .replace
df.replace([224],[24], inplace=True) # il parametro inplace=True ci permette di sovrascrivere la variabile del datafrme, cosi salviamo direttamente la modifica
 
df.replace([330],[30], inplace=True) 





df['mark1'].fillna(df['mark1'].mean(),inplace=True)
# Ho sostituito i NaN della variabile mark1 con la media di quella colonna (dopo aver sistemato gli outliers che altrimenti mi sminchiano la media)
df['mark2'].fillna(df['mark2'].mean(),inplace=True)
df['mark3'].fillna(df['mark3'].mean(),inplace=True)
# e facciamo la stessa cosa con le variabili mark2 d mark3

# Ora dobbiamo ricodificare le variabili non numeriche (gender e fres)

# scriviamo una funzione per gestire la variabile gender
def ricodifica_gender(gender):
    if gender != 'm' or gender != 'f':
        return 0
    else:
        return gender
    
df['gender_recod']=df.gender.apply(ricodifica_gender)
print(df)
    
#modifichiamo l'ultima variabile con la funzione lambda


df['fres_recod']=df.fres.apply(lambda x: x.replace('negative','0'))
df['fres_recod']=df.fres.apply(lambda x: x.replace('pos','1'))
df['fres_recod']=df.fres.apply(lambda x: x.replace('positive','1'))
df['fres_recod']=df.fres.apply(lambda x: x.replace('neg','0'))

print(df)

print('\n normalizzazione dei dati \n')

#
# _ 4.3 _ NORMALIZZAZIONE DEI DATI
#

# In base al nostro modello predittivo che costruiremo, specie se basato sulla distanza, dovremo prima
# provvedere a normalizzare i nostri dati, cioè trasformare tutti i dati in valori compresi tra un 
# range fisso, ad esempio tra 0 e 1.
# Abbiamo 2 tipi principali di normalizzazione, la min-max e la standardizzazione.

np.random.seed(12345)
dfr = pd.DataFrame(np.random.randint(200,size = (10,6))) # creiamo un dataframe di numeri interi da 0 a 200
                                                         # per un totale di 10 casi e 6 variabili

print(dfr)

# normalizzazione min-max : --->   x_norm = (x-min(x)) / (max(x)-min(x))
print('')
dfr_norm = (dfr - dfr.min())/(dfr.max()-dfr.min())
print(dfr_norm)   # Abbiamo ottenuto valori compresi tra 0 e 1 


print('\n standardizzazione \n')

# Ci sarebbe da importare il modulo per la standardizzazione : --->   x_std = x-mean(x) / std(x)
# Ma abbiamo gia in line 43 importato preprocessing da scikitlearn

print(preprocessing.scale(dfr)) 
print('\n') ###  abbiamo standardizzato il dataframe e trasformato il dataframe in array

dfr_scaler = preprocessing.MinMaxScaler(feature_range=(0,1)) ### tramite questo metodo possiamo decidere noi il range entro il quale standardizzare i dati

dfr_scaled = dfr_scaler.fit_transform(dfr)

print(dfr_scaled)

# I dati standardizzati semplificano la ricerca degli outliers

plt.boxplot(dfr_scaled)  # abbiamo soltanto un outlier il quale si trova nella variabile 4

#
# _ 4.4 _ CODIFICA DI UNA VARIABILE CATEGORICA
#

# Vediamo come codificare una variabile categorica in una numerica tramite sklearn

d = pd.DataFrame({'Names': ['Lillo','Cucci','Iron','Renè','Laura','Simon','Laura'],
                  'Height':[176,170,80,38,160,180,160],'Weight':[70,34.5,60,14,57,75,57],
                  'Pref_Food':['Pizza del Paolo','Pasta al forno','Carne','Mango','Crispy mcBacon','Carbonara','Crispy mcBacon'],'Sex':['m','f','m','m','f','m','f']})


print(d)

print('\n')

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

d.iloc[:,3] = LabelEncoder().fit_transform(d.iloc[:,3]) 
# In questa maniera codifichiamo una delle variabili, in particolare la var 3, cioè 'Sex'

# A 'primo membro' abbiamo selezionato la variabile e quindi la traformiamo in una var numerica col secondo membro

# vediamo la variabile
print(d)  # non va, la variabile sex rimane uguale

d.iloc[:,2] = LabelEncoder().fit_transform(d.iloc[:,2]) 
print(d)
# Stavolta non ho più una codifica binaria di zeri e uni ma va da 0 a 4 perchè ho 4 casi


print('\n Variabili dummies \n') 

#
# _ 4.5_ CREAZIONI DI VARIABILI DUMMIES
#

# Consideriamo sempre il solito dataset con i cibi ecc.. ma senza la codifica appena fatta
D = pd.DataFrame({'Names': ['Lillo','Cucci','Iron','Renè','Laura','Simon','Laura'],
                  'Height':[176,170,80,38,160,180,160],'Weight':[70,34.5,60,14,57,75,57],
                  'Pref_Food':['Pizza del Paolo','Pasta al forno','Carne','Mango','Crispy mcBacon','Carbonara','Crispy mcBacon'],'Sex':['m','f','m','m','f','m','f']})


# Per trattare le variabili qualitative (categoriche, non numeriche)
# Possiamo come abbiamo appena visto codificarle, oppure possiamo anche traformarle in variabili dummy
# Cioè ad es. al posto dellla var 'Sex' avremo 2 variabili, entrambe binarie, una sex_m dove avremo 
# 1 per i casi maschili (cioè 'm') e 0 per i femminili e l'altra sex_f, completamente analoga.

D_dummy = pd.get_dummies(d['Sex'], prefix = 'Sex')
print(D_dummy)

# Abbiamo creato un nuovo DataFrame con solo 2 variabili (le dummies)

# Ed ora lo uniamo al dataframe originale con il metodo .join(dataframe)

D2 = D.join(D_dummy)
print('\n')
print(D2)
print('\n')

# A questo punto possiamo ad es. togliere la variabile originale 'Sex' così:

del D2['Sex']  
print(D2)

    









