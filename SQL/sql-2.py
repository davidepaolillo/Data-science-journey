# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 01:02:08 2026

@author: lilpao
"""

import sqlite3
import os

os.chdir(r"C:\Users\lilpao\OneDrive\Desktop\Data-science-journey\progetto-house-pricing")
print(os.getcwd())

import pandas as pd

# carica di nuovo il csv originale (non quello encodato)
df = pd.read_csv("train.csv")

# crea (o apri) un file di database SQLite
conn = sqlite3.connect("house_prices.db")

# !!! Abbiamo creato il database house_prices --> conn è un oggetto python che mi permette di
#     comunicare con il database

# scrive il DataFrame come tabella SQL dentro il database
df.to_sql("houses", conn, if_exists="replace", index=False)

quartieri_info = pd.DataFrame({
    "Neighborhood": ["CollgCr", "Veenker", "Crawfor", "NoRidge", "Mitchel",
                      "Somerst", "NWAmes", "OldTown", "BrkSide", "Sawyer"],
    "Fascia": ["Media", "Alta", "Media", "Alta", "Media",
               "Alta", "Media", "Bassa", "Bassa", "Media"],
    "DistanzaCentro_km": [3.2, 5.1, 2.8, 6.0, 4.5, 5.5, 4.0, 1.5, 1.8, 4.2]
})

quartieri_info.to_sql("quartieri", conn, if_exists="replace", index=False)

"""Ora ho due tabelle collegate dalla colonna Neighborhood: houses (le singole abitazioni) e quartieri
 (info aggregate sui quartieri). Nota: ho inserito solo alcuni quartieri di esempio, non tutti quelli presenti in houses— è voluto, serve tra poco per capire una distinzione importante."""
 
"""
LEZIONE 3- JOIN
Un JOIN prende due tabelle e le unisce riga per riga, abbinando le righe che condividono lo stesso valore
in una colonna comune (qui: Neighborhood). È concettualmente identico a pd.merge() in Pandas, se lo conosci — stessa idea, sintassi diversa.
""" 

#INNER JOIN — il più comune:
    
    
query = """
SELECT c.Neighborhood, c.SalePrice, q.Fascia, q.DistanzaCentro_km
FROM houses AS c
INNER JOIN quartieri AS q ON c.Neighborhood = q.Neighborhood
LIMIT 10
"""

# !!! ON c.Neighborhood = q.Neighborhood → dice la regola di abbinamento: prendi le righe di case e quartieri che hanno lo stesso valore di Neighborhood
# si poteva usare anche l'operatore like al posto dell'=

print(pd.read_sql(query, conn))
 
"""
 Il punto cruciale da capire su INNER JOIN: restituisce solo le righe che trovano corrispondenza in entrambe le tabelle. Dato che quartieri ha solo 10 quartieri su tutti quelli presenti in case, tutte le case degli altri quartieri (es. Gilbert, Timber, ecc.) spariscono completamente dal risultato — non è un bug, è il comportamento esatto di INNER JOIN.
"""
# verifichiamo questa cosa contando le righe

# 1- conta le righe di houses

print(pd.read_sql("SELECT COUNT(*) FROM houses", conn))

# 2- conta le righe dopo il join

print(pd.read_sql("SELECT COUNT(*) FROM houses as c INNER JOIN  quartieri as q ON c.Neighborhood = q.Neighborhood",conn))


"""
Lezione 4 — LEFT JOIN

Ora vediamo come risolvere il "problema" di INNER JOIN: e se invece voglio tenere tutte le case, anche quelle nei quartieri che non hai nella tabella quartieri?
"""