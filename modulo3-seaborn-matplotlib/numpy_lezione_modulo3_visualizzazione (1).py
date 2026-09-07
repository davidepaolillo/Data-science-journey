"""
MODULO 3 - Visualizzazione: Matplotlib e Seaborn
==================================================
Matplotlib e' la libreria base per fare grafici in Python. Seaborn e'
costruita SOPRA Matplotlib, pensata per lavorare direttamente con
DataFrame Pandas (passi data=df e i nomi delle colonne, non i valori
estratti a mano).

Esegui questo file (python numpy_lezione_modulo3.py) - salva i grafici come
immagini .png nella stessa cartella invece di aprirli a schermo, cosi'
funziona anche da terminale puro. Aprili con un visualizzatore immagini
per vederli.

Serve il dataset vendite_negozio.csv nella stessa cartella (quello del
lab Pandas del Modulo 1).
"""

import matplotlib
matplotlib.use("Agg")  # backend non interattivo: necessario per salvare su file senza schermo
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# ============================================================
# 1. ANATOMIA DI UN GRAFICO: FIGURE E AXES
# ============================================================
# Ogni grafico Matplotlib ha una FIGURE (il "foglio" intero) e uno o piu'
# AXES (il singolo riquadro dove disegni - NON e' plurale di "asse").

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]
ax.plot(x, y)   # disegna una linea che collega i punti (x,y)

plt.savefig("modulo3_01_base.png")
plt.close()   # libera la memoria - buona abitudine quando generi molti grafici


# ============================================================
# 2. TITOLI, ETICHETTE, LEGENDA, PIU' LINEE INSIEME
# ============================================================
fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y1 = [10, 25, 15, 30, 20]
y2 = [5, 15, 25, 10, 30]

# Piu' linee sullo stesso ax, con un "label" ciascuna per la legenda
ax.plot(x, y1, color="steelblue", marker="o", label="Negozio A")
ax.plot(x, y2, color="darkorange", marker="s", label="Negozio B")

ax.set_title("Vendite settimanali")
ax.set_xlabel("Settimana")
ax.set_ylabel("Vendite (unita')")
ax.legend()                 # mostra la legenda, usando i "label" definiti sopra
ax.grid(True, alpha=0.3)    # griglia leggera, piu' facile leggere i valori

plt.savefig("modulo3_02_linee_legenda.png")
plt.close()


# ============================================================
# 3. TIPI DI GRAFICO BASE: BARRE, SCATTER, ISTOGRAMMA
# ============================================================
# Regola pratica per scegliere il grafico giusto:
#   - BARRE     -> confronti tra categorie discrete (prodotti, negozi, gruppi)
#   - SCATTER   -> relazione tra due variabili numeriche continue
#   - ISTOGRAMMA -> come si distribuisce UNA sola variabile numerica

# subplots(righe, colonne) crea PIU' Axes in una griglia nella stessa Figure
fig, axes = plt.subplots(1, 3, figsize=(15, 4))  # 1 riga, 3 colonne, dimensione in pollici

categorie = ["A", "B", "C", "D"]
valori = [23, 45, 12, 38]
axes[0].bar(categorie, valori, color="teal")
axes[0].set_title("Grafico a barre")

np.random.seed(0)
x = np.random.rand(50) * 10
y = x * 2 + np.random.randn(50) * 2   # relazione lineare + un po' di rumore
axes[1].scatter(x, y, alpha=0.6)
axes[1].set_title("Scatter plot")

dati = np.random.randn(1000)   # 1000 numeri casuali da una distribuzione normale
axes[2].hist(dati, bins=30, color="coral")
axes[2].set_title("Istogramma")

plt.tight_layout()  # evita che titoli/etichette si sovrappongano tra i subplot
plt.savefig("modulo3_03_tipi_base.png")
plt.close()


# ============================================================
# 4. SEABORN SU UN DATAFRAME PANDAS
# ============================================================
# Qui uso il dataset vendite_negozio.csv dal lab del Modulo 1.
# Con Seaborn passo "data=df" e i NOMI delle colonne, niente estrazione manuale.

df = pd.read_csv("vendite_negozio.csv", parse_dates=["data"])
df["sconto_pct"] = df["sconto_pct"].fillna(0)
df["ricavo"] = df["prezzo_unitario"] * df["quantita"] * (1 - df["sconto_pct"] / 100)

fig, axes = plt.subplots(1, 3, figsize=(16, 4))

# Pre-aggrego con groupby prima di passare a sns.barplot: cosi' evito il
# parametro per le barre d'errore (si chiama "errorbar" nelle versioni
# recenti di Seaborn, "ci" in quelle piu' vecchie - nomi diversi a seconda
# della versione installata). Aggregando prima a mano, il problema non si pone.
ricavo_per_negozio = df.groupby("negozio")["ricavo"].mean().reset_index()
sns.barplot(data=ricavo_per_negozio, x="negozio", y="ricavo", ax=axes[0])
axes[0].set_title("Ricavo medio per negozio")
axes[0].tick_params(axis="x", rotation=20)

sns.boxplot(data=df, x="categoria", y="ricavo", ax=axes[1])
axes[1].set_title("Distribuzione ricavo per categoria")
axes[1].tick_params(axis="x", rotation=20)

sns.histplot(data=df, x="ricavo", hue="categoria", ax=axes[2], element="step")
axes[2].set_title("Distribuzione ricavi, per categoria")

plt.tight_layout()
plt.savefig("modulo3_04_seaborn.png")
plt.close()

# NOTA sul BOXPLOT (uno dei grafici piu' usati in EDA, spiegazione completa):
#   - la linea nel mezzo del box = la MEDIANA
#   - il box copre dal 25* al 75* percentile (il "grosso" dei dati)
#   - i "baffi" (le lineette che escono dal box) arrivano fino agli estremi normali
#   - i pallini isolati oltre i baffi = OUTLIER (valori anomali)


# ============================================================
# 5. HEATMAP DI CORRELAZIONE
# ============================================================
# .corr() calcola la correlazione tra OGNI coppia di colonne numeriche
# (valore tra -1 e 1: vicino a 1 = correlazione positiva forte, vicino a
# -1 = correlazione negativa forte, vicino a 0 = nessuna relazione lineare)

correlazioni = df[["prezzo_unitario", "quantita", "sconto_pct", "ricavo"]].corr()
print(correlazioni)

plt.figure(figsize=(6, 5))
sns.heatmap(correlazioni, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlazione tra variabili numeriche")
plt.tight_layout()
plt.savefig("modulo3_05_heatmap.png")
plt.close()


# ============================================================
# RIEPILOGO MODULO 3
# ============================================================
print("""
RIEPILOGO
---------
Struttura base       -> fig, ax = plt.subplots(), poi ax.plot(), plt.savefig()
Titoli/etichette      -> ax.set_title(), ax.set_xlabel(), ax.legend(), ax.grid()
Tipi di grafico       -> ax.bar() (categorie), ax.scatter() (relazione tra 2 var), ax.hist() (distribuzione di 1 var)
Piu' grafici insieme  -> plt.subplots(righe, colonne) -> restituisce un array di ax
Seaborn su DataFrame  -> sns.barplot/boxplot/histplot(data=df, x=..., y=...)
Boxplot               -> mediana, box=25*-75* percentile, baffi, pallini=outlier
Correlazione          -> df.corr() + sns.heatmap(annot=True)
""")


# ============================================================
# ESERCIZIO PRATICO
# ============================================================
# Usando sempre vendite_negozio.csv (df e' gia' definito sopra con la colonna ricavo):
#
# 1) Crea un grafico a barre con il RICAVO TOTALE (non medio) per ogni categoria
#    (suggerimento: prima raggruppa con groupby+sum, poi passa il risultato a
#     sns.barplot oppure a plt.bar)
#
# 2) Crea uno scatter plot con prezzo_unitario sull'asse x e ricavo sull'asse y,
#    colorando i punti in base al negozio (suggerimento: sns.scatterplot ha un
#    parametro hue=, come histplot sopra)
#
# 3) Crea un istogramma della sola colonna quantita, per farti un'idea di come
#    si distribuiscono le quantita' vendute per transazione
#
# Scrivi qui sotto il tuo codice:
