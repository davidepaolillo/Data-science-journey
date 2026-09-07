
# -*- coding: utf-8 -*-

# IMPORTARE E MANIPOLARE UN DATASET
#
# In questa lezione vedremo come importare un Dataset con Pandas, inoltre vediamo alcune funzioni utili di Pandas per maneggiare il file
# 
#

import pandas as pd
df=pd.read_csv('df.csv')
print(df)


#
#pd.read_csv('df.csv',header=None) per saltare la prima riga
#pd.read_csv('df.csv',header=0) per saltare la riga che voglio (sempre la prima in questo caso)
#pd.read_csv('df.csv',usecols=[0,1,2,3]) per dirgli che colonne voglio usare (quindi posso eliminare una o più colonne)
#df.head(2) cosi analogamente gli sto dicendo di prendere solo le prime 3 righe
#
print('\n \n tolte le ultime due colonne')

azz=pd.read_csv('df.csv',usecols=[0,1,2,3])
print(azz)

# Per riassumere il campione si può usare il metodo .describe() ottendendo media, dev std ecc..
print(df.describe())

# Pandas e in particolare il metodo .read si possono usare anche per importare dei dataset dal web, ad es. scrivendo UCI machine learning su google (sito con vari dataset)
# e cliccando sul nome, poi data folder, e poi tasto destro su nome.data copiando quindi il link e incollandolo qui in questo modo :

iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
# vediamo le prime righe di questo file 
print(iris.head(5))

#iris.to_csv('nome che voglio') in questo modo prendo il file e me lo salva nella working directory come file CSV


   #
# Altri metodi sono:
    # pd.read_table('link')  ---> fa la stessa cosa, legge tutto il file
    # pd.read_excel('link.xlsx', 'nome foglio')  ---> ci permette di leggere un file excel, ma dobbiamo aggiungere il parametro del nome del foglio da importare
    # df.to_excel()  ---> analoga a quella del csv
   #
   
   
# Abbiamo anche altre funzioni analoghe per importare dataset .html e .json   pd.read_html('nome.html') e pd.read_json('nome.json')





print(' \n \n Ora vediamo come manipolare un dataset con Pandas')

# Per prima cosa creiamo un Dataframe in questo modo
df1=pd.DataFrame({'Names': ['Lillo','Cucci','Iron','Renè','Laura','Simon','Laura'],
                  'Height':[176,170,80,38,160,180,160],'Weight':[70,34.5,60,14,57,75,57],
                  'Pref_Food':['Pizza del Paolo','Pasta al forno','Carne','Mango','Crispy mcBacon','Carbonara','Crispy mcBacon'],'Sex':['m','f','m','m','f','m','f']})

print(df1)
# Possiamo sempre usare il metodo .Describe
print(df1.describe())

print(df1.dtypes) # Per vedere se ho interi, floats, ecc...

print(df1.shape)  # Mi da una coppia con il numero di casi e di variabili (nomi,altezza,peso,cibo preferito)

# Possiamo ottenere queste informazioni (date da .dtypes e da .shape anche con il metodo .info)

print(df1.info())

#df1.set_index('Names',inplace = True) # Per settare un indice
#print(df1)                            
                                      # Lo slicing si puo comunque fare uguale
print(df1[2:])


#Per ordinare il dataset in base ad una variabile (es. peso)

print(df1.sort_values(by = 'Weight')) # NON ha sovrascritto la variabile df1, la quale  è rimasta NON ordinata tramite il peso

print('\n\n ora i metodi .loc, .iloc, .ix')

#print(df1.loc['Cucci']) # Se non indicizzavo per Names dovevo mettere il numerino

print('\n')


print(df1.iloc[1,2])    # Prende il secondo indice (che corrisponde a 1 ) e ne prende la terza colonna (che corrisponde al 2)
                        # restituisce pasta al forno


# ix non mi va


print('\n\n Condizioni di estrazione \n\n') 

print(df1[df1.Height>100])
print('\n\n')
print(df1[df1['Pref_Food']== 'Pizza del Paolo'])

print('\n\n Per creare una nuova colonna')

df1['new col']=df1.Height/100
print(df1)  # Così abbiamo le altezze in metri

print('\n\n per creare dei gruppi')

g1=df1.groupby('Sex')
print(g1.groups)
print('\n')
print(g1.describe())

print('\n\n Vediamo come creare variabili dummies')
df1_dummy = pd.get_dummies(df1['Sex'], prefix = 'Sex')
print(df1_dummy)
# A questo punto possiamo unire le due variabili dummies al dataset originale tramite join

dff=df1.join(df1_dummy) # non sovrascrive la variabile
print(dff)

#Voglio cancellare una colonna e tornare al dataset originale
print('\n\n per cancellare una colonna \n')
del df1['new col']
print(df1)

print('\n\n ora vediamo come cancellare i dati doppi \n\n')

#
# Prima di tutto con .duplicated() possiamo vedere se ci sono dei doppioni
#

print(df1.duplicated())  # nel 6 esce True perchè l'ultimo caso è duplicato

#
# A questo punto creiamo un nuovo dataframe eliminando i duplicati
#

df2=df1.drop_duplicates()
print(df2)   # Ha eliminato la riga ripetuta di Laura

print('\n\n stack()  melt() e T \n')
# Si possono riorganizzare i dati con le funzioni df1.stack e df1.melt
print(df2.melt())
print('\n')
# Con la funzione T invertiamo righe e colonne, cioè i casi diventano variabili  e le variabili diventano casi
print(df1.T) # quando poi faccio ad esempio lo sclicing non posso più farlo con i numeri (penso)

print('\n\n ')

print('per estrarre elementi dal dataframe')

print('\n se scrivo df1.sample(3) mi fa un dataframe con 3 elementi a caso estratti da df1')

import numpy as np  # impostiamo un seed

np.random.seed(1)  
# cosi mi estrae sempre gli stessi 2 perchè ho impostato il seed
print(df1.sample(2))

print('\n')

# al posto di prenderne due a caso posso prendere una percentuale del dataframe
print(df1.sample(frac=0.4))

print('\n Ora apriamo un nuovo dataset con degli elementi mancanti \n')

df_missing=pd.read_csv('df_missing.csv')
print(df_missing) # dove ci sono dei valori mancanti c'è  la scritta NaN
print('\n')
#df_missing.dropna().shape
#così visualizzo la coppia (i casi completi, cioè senza elementi mancanti ; e il numero di variabili)

print(pd.isnull(df_missing)) # mi dà la tabella completa del dataframe con True (se il valore è mancante) e False (se il valore c'è)

# speculare è il metodo .notnull

print('\n togliamo le righe o le colonne con elementi mancanti \n')

print(df_missing.dropna())  # rimangono solo le righe senza NaN

print(df_missing.dropna(axis=1, how ='any')) # salviamo le colonne che non contengono dati mancanti

print('\n IMPORTANTE: Per inserire un valore al posto dei dati mancanti si usa sempre fillna')
 
print(df_missing.fillna(0)) # in questo caso inseriamo lo zero, potevamo inserire ad esempio la dicitura 'missing'


print('\n al posto dello zero si può mettere una media dei dati di quella colonna (variabile) !!!')

print(df_missing.fillna(df_missing.mean()))

print(' \n per dare la media di una sola variabile scrivo così \n')

# Ho isolato la colonna della variabile C 

print(df_missing['C'].fillna(df_missing['C'].mean()))


#In pratica fillna sostituisce i valori mancanti (NaN) con un valore a tua scelta. Il pattern è:
#df["colonna"] = df["colonna"].fillna(valore_da_usare)
# Claude ---> df["stipendio"]=df["stipendio"].fillna(df["stipendio"].mean())





print('\n ffill e backfill')
# Altri due metodi sono ffil e backfil

#ffil rimpiazza il valore mancante con il valore non mancante che lo precede (nella colonna, cioè il caso precedente di quella variabile)
#backfill rimpiazza il valore mancante con il valore non mancante che lo segue

print(df_missing['C'].fillna(method='ffill'))
                                                 # Ragioniamo sempre su una vairabile e usiamo sempre fillna
print(df_missing['C'].fillna(method='backfill'))




















