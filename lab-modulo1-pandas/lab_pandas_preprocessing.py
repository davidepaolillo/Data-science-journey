"""
LAB PANDAS - PREPROCESSING DI UN DATASET
==========================================
Dataset: dataset_immobili.csv (annunci immobiliari fittizi, generato ad hoc,
non è un dataset "vero" trovato online, ma è costruito per farti allenare
esattamente sulle situazioni che hai incontrato nel progetto House Prices).

Colonne del dataset:
- Id: identificativo dell'annuncio
- Superficie_mq: superficie in metri quadri (con qualche missing e qualche outlier)
- Piano: piano dell'appartamento
- NumeroBagni: numero di bagni
- AnnoCostruzione: anno di costruzione (con qualche missing)
- Quartiere: zona della città (categorica)
- TipoRiscaldamento: tipo di riscaldamento (categorica, con missing)
- Giardino: presenza giardino Si/No (categorica, con missing)
- Ascensore: presenza ascensore Si/No (categorica, nessun missing)
- Prezzo: prezzo di vendita (target)

ISTRUZIONI: sotto ogni esercizio trovi una spiegazione di cosa fare.
Scrivi il codice nello spazio indicato. Non ci sono soluzioni nel file:
quando hai fatto (tutti o alcuni esercizi), mandami il tuo codice/output
e lo correggiamo insieme.
"""

import pandas as pd
import numpy as np

df = pd.read_csv("dataset_immobili.csv")


# ============================================================
# ESERCIZIO 1 - Esplorazione iniziale
# ============================================================
# Stampa:
# a) le dimensioni del dataset (righe, colonne)
# b) info() per vedere tipi di dato e conteggio valori non-null
# c) describe() per le statistiche delle colonne numeriche
# d) le prime 5 righe

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 2 - Missing values: individuarli e classificarli
# ============================================================
# a) Trova quali colonne hanno valori mancanti e quanti (in ordine decrescente)
# b) Per ciascuna colonna con missing, stabilisci se è categorica o numerica
#    (hint: usa .dtype oppure select_dtypes)
# c) Rifletti (puoi scriverlo come commento nel codice): in questo dataset,
#    ha senso pensare che qualche NaN rappresenti "l'informazione non è
#    stata specificata" piuttosto che "dato numerico da stimare"? Quali
#    colonne ti sembrano più indicate per un trattamento diverso dalla
#    semplice media/mediana?

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 3 - Gestione dei missing
# ============================================================
# a) Per le colonne CATEGORICHE con missing, sostituisci i NaN con una
#    categoria esplicita "Non specificato"
# b) Per le colonne NUMERICHE con missing, sostituisci i NaN con la
#    MEDIANA della colonna (motiva a parole, nel commento, perché la
#    mediana è spesso preferibile alla media in presenza di outlier)
# c) Verifica alla fine che non ci siano più missing nel dataset
#    (somma totale dei NaN deve fare 0)

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 4 - Individuare outlier con il metodo IQR
# ============================================================
# Richiamo teorico: il metodo IQR (Interquartile Range) definisce come
# outlier i valori che escono dall'intervallo:
#   [Q1 - 1.5*IQR ,  Q3 + 1.5*IQR]
# dove Q1 = 25° percentile, Q3 = 75° percentile, IQR = Q3 - Q1
#
# a) Calcola Q1, Q3 e IQR per la colonna Superficie_mq
# b) Costruisci una maschera booleana che individua le righe outlier
#    secondo la formula sopra
# c) Stampa quante righe sono outlier e stampale (dovresti ritrovare
#    proprio quelle con superficie "esplosa" per errore)

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 5 - Correggere gli outlier
# ============================================================
# Una volta individuati gli outlier del punto 4, decidi un trattamento:
# ad esempio sostituiscili con la MEDIANA della colonna (oppure, se
# preferisci, con NaN e poi fillna come nell'esercizio 3 - a tua scelta,
# ma motivalo in un commento)

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 6 - Feature engineering
# ============================================================
# Crea le seguenti nuove colonne, sul modello di quanto fatto nel
# progetto House Prices:
# a) EtaImmobile = 2026 - AnnoCostruzione  (età dell'immobile ad oggi)
# b) PrezzoAlMq = Prezzo / Superficie_mq   (prezzo al metro quadro,
#    utile per confrontare immobili di dimensioni diverse)
# c) ContaComfort = quante tra le colonne "Giardino"/"Ascensore" hanno
#    valore "Si" (hint: puoi sommare due condizioni booleane convertite
#    a int, come abbiamo fatto per HasGarage/HasPool)

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 7 - GroupBy
# ============================================================
# a) Calcola il prezzo medio per Quartiere, ordinato dal più caro al
#    più economico
# b) Calcola, per ogni Quartiere, sia il prezzo medio che il PrezzoAlMq
#    medio (hint: .agg() con un dizionario, oppure .agg(['mean']) su
#    più colonne insieme)
# c) Calcola il prezzo medio raggruppando per Quartiere E Ascensore
#    insieme (groupby con una lista di due colonne)

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 8 - One-Hot Encoding
# ============================================================
# a) Individua le colonne categoriche del dataset (dopo i fillna
#    dell'esercizio 3)
# b) Applica pd.get_dummies con drop_first=True
# c) Stampa lo shape del dataset prima e dopo l'encoding: quante
#    colonne sono state aggiunte?

# --- scrivi qui ---


# ============================================================
# ESERCIZIO 9 (bonus, più aperto) - Correlazione con il target
# ============================================================
# Calcola la correlazione tra tutte le colonne numeriche e Prezzo
# (hint: df.corr()["Prezzo"], oppure .corr() su tutto il dataset e poi
# selezioni la colonna Prezzo). Ordina i risultati e commenta (nel
# codice, come commento) quali 2-3 variabili sembrano più legate al
# prezzo, e se il risultato ti sembra sensato rispetto a come abbiamo
# costruito il dataset.

# --- scrivi qui ---
