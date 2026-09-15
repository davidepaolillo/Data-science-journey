# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 23:06:50 2026

@author: lilpao
"""

import sqlite3
import pandas as pd
import os

os.chdir(r"C:\Users\lilpao\OneDrive\Desktop\Data-science-journey\progetto-house-pricing")
print(os.getcwd())



"""

SQL                     Pandas
-----------------------------------------
SELECT                  scelta colonne
WHERE                   filtro righe
GROUP BY                groupby()
ORDER BY                sort_values()
JOIN                    merge()
COUNT / AVG / SUM       count / mean / sum
HAVING                  filtra righe dopo un GROUP BY (cioè filtra tra i gruppi)

"""






"""
LEZIONE 1- SQL lite, SELECT, FROM, WHERE
"""

# carica di nuovo il csv originale (non quello encodato)
df = pd.read_csv("train.csv")

# crea (o apri) un file di database SQLite
conn = sqlite3.connect("house_prices.db")

# !!! Abbiamo creato il database house_prices --> conn è un oggetto python che mi permette di
#     comunicare con il database

# scrive il DataFrame come tabella SQL dentro il database
df.to_sql("houses", conn, if_exists="replace", index=False)

#if_exists="replace"significa: se nel database esiste già una tabella chiamata houses, cancellala e ricreala usando questo DataFrame.
#index=False dice di non salvare l'indice Pandas come colonna SQL
"""
to_sql è un metodo di Pandas che fa da "ponte": prende un DataFrame e lo scrive come tabella dentro un database SQL. 
Ho chiamato la tabella houses. 
"""

query = "SELECT * FROM houses LIMIT 5"
risultato = pd.read_sql(query, conn)
print(risultato)

"""
SELECT * → "seleziona tutte le colonne" (l'asterisco è un jolly che significa "tutto")
FROM houses → "dalla tabella chiamata case (un database ha di solito tante tabelle"
LIMIT 5 → "restituisci solo le prime 5 righe" (fondamentale con tabelle grandi, altrimenti rischio di stampare milioni di righe)
"""

# 1) Solo alcune colonne, non tutte
query1 = "SELECT Neighborhood, SalePrice, YearBuilt FROM houses LIMIT 10"
print(pd.read_sql(query1, conn))

# 2) Con un filtro (WHERE) e un ordinamento (ORDER BY)
query2 = "SELECT Neighborhood, SalePrice FROM houses WHERE SalePrice > 300000 ORDER BY SalePrice DESC"
print(pd.read_sql(query2, conn))


# Quindi WHERE funziona un po' come una condizione: df[df["saleprice"] > 300000]








"""
Lezione 2 — GROUP BY e funzioni di aggregazione: -->
SUM()
COUNT()
MIN()
MAX()
AVG()
"""
# è esattamente lo stesso concetto del groupby di pandas


Query = """
SELECT Neighborhood, AVG(SalePrice) AS prezzo_medio
FROM houses
GROUP BY Neighborhood
ORDER BY prezzo_medio DESC
"""
print(pd.read_sql(query, conn))

#spiegazione della Query

"""
AVG(SalePrice) AS prezzo_medio → calcola la media di SalePrice; AS è semplicemente un modo per rinominare la colonna risultato (altrimenti si chiamerebbe automaticamente AVG(SalePrice), scomodo da leggere)


GROUP BY Neighborhood → stampa n righr, una per ogni valore distinto di Neighborhood, e applica l'aggregazione (AVG) dentro ogni gruppo separatamente
per riassumere quel quartiere

È molto simile a Pandas --> df.groupby("Neighborhood")["SalePrice"].mean()

TRADOTTO IN ITALIANO SAREBBE: "Per ogni quartiere, calcola il prezzo medio delle case e mostrami
 i quartieri ordinati dal più costoso al meno costoso""

"""


"""
Un concetto importante da capire subito: SELECT con GROUP BY ha una regola rigida.

Quando usi GROUP BY, nel SELECT puoi mettere solo:

le colonne su cui hai raggruppato (Neighborhood)
funzioni di aggregazione (AVG(...), COUNT(...), ecc.)

Non puoi aggiungere altre colonne "a caso" (es. YearBuilt) perché SQL non saprebbe quale valore mostrare per quella colonna, dato che dentro ogni gruppo ci sono più righe con YearBuilt diversi. Questo è diverso da Pandas, dove groupby è un po' più permissivo di primo acchito — in SQL questa regola è rigida e dà errore se la violi.
dopo un GROUP BY, SQL vuole costruire una sola riga di output per ogni gruppo.
Se mi interessa anche year built devo aggregare anche quello --> es. con la media e otterrei

Neighborhood   anno_medio   prezzo_medio
NAmes           1980         180000
CollgCr         2000         235000
.
.
.

"""


# 1) Quante case ci sono per ogni quartiere?



Query1 = "SELECT Neighborhood, COUNT(*) AS numero_case FROM houses GROUP BY Neighborhood ORDER BY numero_case DESC"

# 2) Prezzo massimo e minimo per numero di camere da letto (BedroomAbvGr)
Query2 = "SELECT BedroomAbvGr, MAX(SalePrice) AS prezzo_max, MIN(SalePrice) AS prezzo_min FROM houses GROUP BY BedroomAbvGr"

# 3) Filtra i quartieri con prezzo medio sopra 200000 (attenzione: qui NON puoi usare WHERE!)
Query3 =" SELECT Neighborhood, AVG(SalePrice) AS Prezzo_Medio FROM houses GROUP BY Neighbourhood HAVING Avg(SalePrice)>20000"



"""
!!!! Ordine logico da ricordare !!!!
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
"""




