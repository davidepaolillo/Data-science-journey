"""
LAB PANDAS - Modulo 1 (consolidamento)
========================================
Dataset: vendite_negozio.csv (150 vendite simulate, gen-giu 2025)
Colonne:
  - data              : data della vendita
  - negozio           : uno tra Milano Centro, Torino Nord, Roma Est, Napoli Sud
  - categoria          : uno tra Elettronica, Abbigliamento, Casa, Sport
  - prezzo_unitario    : prezzo del singolo articolo (euro)
  - quantita           : unita' vendute in quella transazione
  - sconto_pct         : sconto applicato in percentuale (0-20, alcuni valori mancanti = NaN)

ISTRUZIONI
----------
Completa ogni funzione qui sotto sostituendo `pass` con il tuo codice.
Non guardare soluzioni online: se ti blocchi, prova, scrivi cosa hai capito
e cosa no, poi lo rivediamo insieme.
Alla fine c'e' un blocco che esegue e stampa il risultato di ogni esercizio,
cosi' puoi controllare da solo se il formato ha senso PRIMA di mandarmelo.

Assicurati che vendite_negozio.csv sia nella stessa cartella di questo file.
"""

import pandas as pd


def carica_dati(path="vendite_negozio.csv"):
    """
    Esercizio 0 (fatto per te, come esempio):
    Carica il CSV in un DataFrame e assicurati che la colonna 'data'
    sia interpretata come data (non come stringa).
    """
    df = pd.read_csv(path, parse_dates=["data"])
    return df


def esercizio_1_esplorazione(df):
    """
    Esplora il dataset. La funzione deve restituire una TUPLA con:
      (numero_di_righe, numero_di_colonne, lista_nomi_colonne)

    Suggerimento: df.shape ti da' (righe, colonne). df.columns ti da' i nomi.
    """
    # TODO: scrivi qui il tuo codice
    return (df.shape[0],df.shape[1],list(df.columns))
    


def esercizio_2_filtro_categoria(df, categoria="Elettronica"):
    """
    Restituisci un DataFrame con SOLO le vendite della categoria indicata
    (default: 'Elettronica'), con prezzo_unitario superiore a 100 euro.

    Suggerimento: puoi combinare due condizioni con l'operatore & (e),
    ricordandoti di mettere ogni condizione tra parentesi, es:
    df[(condizione1) & (condizione2)]
    """
    # TODO: scrivi qui il tuo codice
    return df[(df["categoria"]==categoria) & (df["prezzo_unitario"] >100)]
    


def esercizio_3_colonna_ricavo(df):
    """
    Aggiungi al DataFrame una nuova colonna 'ricavo' calcolata come:
      ricavo = prezzo_unitario * quantita * (1 - sconto_pct/100)

    Attenzione: sconto_pct ha dei valori mancanti (NaN). Se fai il calcolo
    direttamente, il ricavo di quelle righe verra' NaN. Prima di calcolare,
    riempi i mancanti di sconto_pct con 0 (nessuno sconto è un'assunzione
    ragionevole in assenza di informazioni).

    Restituisci il DataFrame con la nuova colonna aggiunta.
    """
    # TODO: scrivi qui il tuo codice
    df= df.fillna(0)
    df["ricavo"]=df["prezzo_unitario"]*df["quantita"]*(1-df["sconto_pct"]/100)
    return df
    
# Qui funziona perche quella dello sconto_pct è l unica colonna con dei NaN, altrimenti dovevo fare
# df["sconto_pct"] = df["sconto_pct"].fillna(0)
# L'altro mette tutti i NaN del df a 0

def esercizio_4_ricavo_per_negozio(df):
    """
    Usando il DataFrame CON la colonna 'ricavo' gia' calcolata (esercizio 3),
    restituisci una Series con il ricavo TOTALE (non la media) per negozio,
    ordinata dal negozio con piu' ricavo a quello con meno.

    Suggerimento: groupby + sum(), poi guarda come hai fatto sort_values
    in un esercizio precedente (funziona anche su una Series).
    """
    # TODO: scrivi qui il tuo codice
    df = df.groupby("negozio")["ricavo"].sum().sort_values(ascending=False)
    return df
# "Raggruppa (groupby) per negozio, poi prendi la colonna ricavo, e per ogni gruppo fai la somma"
# qui tutte le righe vengono usate, solo raggruppate e poi riassunte con un numero per gruppo.
# Poi con sort_values lo ordiniamo
# Su una Series c'è una sola colonna di dati, quindi non ha senso dirle "ordina in base alla colonna ricavo" — quella colonna è l'unica cosa che c'è.

def esercizio_5_doppio_raggruppamento(df):
    """
    Restituisci il ricavo medio raggruppato SIA per negozio SIA per categoria
    (raggruppamento su due livelli).

    Suggerimento: groupby puo' accettare una LISTA di colonne invece di una
    sola stringa: df.groupby(["colonna1", "colonna2"])
    """
    df = df.groupby(["negozio","categoria"])['ricavo'].mean().sort_values()
    return df
# è sempre una series ma con un doppio indice

def esercizio_6_top_transazioni(df):
    """
    Restituisci le 5 transazioni con il ricavo piu' alto in assoluto
    (l'intero DataFrame, tutte le colonne, solo le prime 5 righe per ricavo).

    Suggerimento: c'e' un metodo pandas che fa "ordina e prendi le prime N"
    in un solo passaggio, si chiama nlargest(N, "colonna"). E' equivalente
    a sort_values(...).head(N) ma piu' diretto.
    """
    df=df.nlargest(5,"ricavo")
    return df


def esercizio_7_conteggio_categorie(df):
    """
    Restituisci quante transazioni ci sono per ciascuna categoria
    (un conteggio semplice, non una somma o una media).

    Suggerimento: esiste un metodo pensato apposta per "contare quante volte
    compare ogni valore distinto in una colonna": value_counts().
    """
    conteggio = df.value_counts("categoria")
    return conteggio


# ============================================================
# NON MODIFICARE DA QUI IN POI: esegue e stampa i tuoi risultati
# ============================================================
if __name__ == "__main__":
    df = carica_dati()
    print("Dataset caricato:", df.shape, "\n")

    print("=== Esercizio 1: esplorazione ===")
    print(esercizio_1_esplorazione(df), "\n")

    print("=== Esercizio 2: filtro categoria ===")
    print(esercizio_2_filtro_categoria(df), "\n")

    df_ricavo = esercizio_3_colonna_ricavo(df)
    print("=== Esercizio 3: colonna ricavo ===")
    print(df_ricavo.head() if df_ricavo is not None else None, "\n")

    print("=== Esercizio 4: ricavo per negozio ===")
    print(esercizio_4_ricavo_per_negozio(df_ricavo) if df_ricavo is not None else None, "\n")

    print("=== Esercizio 5: doppio raggruppamento ===")
    print(esercizio_5_doppio_raggruppamento(df_ricavo) if df_ricavo is not None else None, "\n")

    print("=== Esercizio 6: top 5 transazioni ===")
    print(esercizio_6_top_transazioni(df_ricavo) if df_ricavo is not None else None, "\n")

    print("=== Esercizio 7: conteggio categorie ===")
    print(esercizio_7_conteggio_categorie(df), "\n")
