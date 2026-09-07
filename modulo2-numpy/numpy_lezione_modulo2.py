"""
MODULO 2 - NumPy: le basi
==========================
NumPy e' la libreria su cui e' costruito Pandas stesso: array multidimensionali
con calcolo VETTORIZZATO, cioe' operazioni che si applicano a interi array
senza scrivere cicli for espliciti (piu' veloce e piu' leggibile).

Esegui questo file dall'inizio alla fine (python numpy_lezione.py) e leggi
l'output insieme ai commenti: ogni sezione introduce UN concetto alla volta.
"""

import numpy as np


# ============================================================
# 1. COS'E' UN ARRAY E COME SI CREA
# ============================================================
print("=" * 60)
print("1. CREAZIONE DI UN ARRAY")
print("=" * 60)

# Un array si crea a partire da una lista Python con np.array()
a = np.array([10, 20, 30, 40])
print("Array:", a)
print("Tipo:", type(a))

# A differenza di una lista Python, un array NumPy ha degli ATTRIBUTI
# che descrivono la sua struttura:
print("\nAttributi dell'array:")
print("shape (forma):", a.shape)          # quante dimensioni e quanti elementi per dimensione
print("dtype (tipo dei dati):", a.dtype)  # TUTTI gli elementi hanno lo stesso tipo (a differenza delle liste!)
print("ndim (numero di dimensioni):", a.ndim)
print("size (numero totale di elementi):", a.size)

# NOTA: una lista Python puo' mescolare tipi diversi, es. [1, "ciao", 3.5].
# Un array NumPy no: se ci provi, NumPy converte tutto a un tipo comune.


# ============================================================
# 2. ARRAY MULTIDIMENSIONALI (MATRICI) E CREAZIONE RAPIDA
# ============================================================
print("\n" + "=" * 60)
print("2. MATRICI E CREAZIONE RAPIDA")
print("=" * 60)

# Un array 2D si crea da una LISTA DI LISTE - ogni lista interna e' una riga
matrice = np.array([[1, 2, 3],
                     [4, 5, 6]])
print("Matrice:")
print(matrice)
print("shape:", matrice.shape)   # (2, 3) = 2 righe, 3 colonne
print("ndim:", matrice.ndim)     # 2 dimensioni

print("\n--- np.zeros: matrice di soli zeri ---")
print(np.zeros((3, 4)))          # 3 righe, 4 colonne, tutti zeri

print("\n--- np.ones: matrice di soli uno ---")
print(np.ones((2, 2)))

print("\n--- np.arange: come range() di Python, ma restituisce un array ---")
print(np.arange(0, 10, 2))       # da 0 a 10 (escluso), passo 2

print("\n--- np.linspace: N numeri equispaziati tra un inizio e una fine (INCLUSI) ---")
print(np.linspace(0, 100, 5))    # 5 numeri equispaziati tra 0 e 100

# DIFFERENZA CHIAVE arange vs linspace:
# - arange(inizio, fine, PASSO): decidi il passo, non sai in anticipo quanti numeri ottieni
# - linspace(inizio, fine, QUANTI): decidi quanti numeri vuoi, include SEMPRE anche l'ultimo


# ============================================================
# 3. INDICIZZAZIONE E SLICING
# ============================================================
print("\n" + "=" * 60)
print("3. INDICIZZAZIONE E SLICING")
print("=" * 60)

a = np.array([10, 20, 30, 40, 50])
print("--- Array 1D (uguale alle liste che gia' conosco) ---")
print("Primo elemento a[0]:", a[0])
print("Ultimo elemento a[-1]:", a[-1])
print("Slice a[1:3]:", a[1:3])

print("\n--- Array 2D: qui cambia la sintassi ---")
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(m)

# Sintassi: m[riga, colonna] - UNA VIRGOLA dentro le stesse parentesi quadre,
# diversa da come indicizzerei una lista di liste in Python puro (lista[1][2])
print("\nElemento riga 1, colonna 2 -> m[1, 2]:", m[1, 2])

print("Tutta la riga 0 -> m[0, :]:", m[0, :])       
print("Tutta la colonna 1 -> m[:, 1]:", m[:, 1])    # tutte le righe, solo colonna indice 1

print("\nSotto-matrice, prime 2 righe e prime 2 colonne -> m[0:2, 0:2]:")
print(m[0:2, 0:2])


# ============================================================
# 4. OPERAZIONI ARITMETICHE VETTORIZZATE (il cuore di NumPy)
# ============================================================
print("\n" + "=" * 60)
print("4. OPERAZIONI VETTORIZZATE")
print("=" * 60)

a = np.array([1, 2, 3, 4])

print("--- Operazioni tra array e un singolo numero (scalare) ---")
print("a + 10:", a + 10)     # somma 10 a OGNI elemento
print("a * 2:", a * 2)       # moltiplica OGNI elemento per 2
print("a ** 2:", a ** 2)     # eleva OGNI elemento al quadrato

print("\n--- Operazioni tra due array della stessa dimensione ---")
b = np.array([10, 20, 30, 40])
print("a + b:", a + b)       # somma elemento per elemento
print("a * b:", a * b)       # moltiplicazione ELEMENTO PER ELEMENTO
# ATTENZIONE: a * b qui NON e' il prodotto scalare/matriciale
# dell'algebra lineare, e' il prodotto "di Hadamard" (elemento per elemento).
# Per il prodotto scalare vero servono np.dot(a, b) oppure l'operatore @

print("\n--- Funzioni matematiche applicate a tutto l'array in un colpo ---")
print("Radice quadrata:", np.sqrt(a))
print("Esponenziale:", np.exp(a))
print("Logaritmo naturale:", np.log(a))


# ============================================================
# 5. AGGREGAZIONI E IL PARAMETRO axis
# ============================================================
print("\n" + "=" * 60)
print("5. AGGREGAZIONI CON axis")
print("=" * 60)

m = np.array([[1, 2, 3],
              [4, 5, 6]])
print("Matrice:")
print(m)

print("\n--- Senza axis: aggrega TUTTO l'array in un solo numero ---")
print("Somma totale:", m.sum())
print("Media totale:", m.mean())

print("\n--- axis=0: aggrega 'lungo le righe', cioe' colonna per colonna ---")
print("Somma per colonna:", m.sum(axis=0))   # 1+4=5, 2+5=7, 3+6=9

print("\n--- axis=1: aggrega 'lungo le colonne', cioe' riga per riga ---")
print("Somma per riga:", m.sum(axis=1))      # 1+2+3=6, 4+5+6=15

# REGOLA MNEMONICA per axis: indica quale dimensione "scompare" nel risultato.
# axis=0 -> scompare l'indice delle RIGHE -> resta un valore per colonna
# axis=1 -> scompare l'indice delle COLONNE -> resta un valore per riga


# ============================================================
# 6. FILTRO BOOLEANO
# ============================================================
print("\n" + "=" * 60)
print("6. FILTRO BOOLEANO")
print("=" * 60)

a = np.array([15, 42, 8, 23, 61, 4, 55])
print("Array:", a)

# !!!!  Una CONDIZIONE su un array restituisce un array di True/False

condizione = a > 20
print("\nCondizione (a > 20):", condizione)

# Usando quell'array di True/False come "indice", NumPy tiene solo i True
print("Elementi che soddisfano la condizione:", a[condizione])
print("Stessa cosa in una riga:", a[a > 20])

# ---> in linea con la sintassi dei dataframe di pandas 


# Posso anche MODIFICARE solo gli elementi che soddisfano una condizione
b = a.copy()   # copio per non modificare l'array originale
b[b > 20] = 0
print("\nSostituiti con 0 gli elementi > 20:", b)

# Contare quanti elementi soddisfano una condizione: sommo i True (contano come 1)
print("Quanti elementi > 20?", (a > 20).sum())


# ============================================================
# RIEPILOGO
# ============================================================
print("\n" + "=" * 60)
print("RIEPILOGO MODULO 2")
print("=" * 60)
print("""
Creare un array    -> np.array([...]), np.zeros((r,c)), np.arange(i,f,passo), np.linspace(i,f,quanti)
Attributi           -> .shape, .dtype, .ndim, .size
Indicizzare 2D       -> m[riga, colonna], m[riga, :], m[:, colonna]
Operazioni           -> + - * / ** elemento per elemento; np.sqrt(), np.exp(), np.log()
Statistiche          -> .sum(), .mean(), .std(), .max(), .min(), con axis=0/axis=1
Filtro booleano      -> array[array > soglia], (array > soglia).sum() per contare
""")


# ============================================================
# ESERCIZIO PRATICO
# ============================================================
# Data questa serie di temperature giornaliere (in gradi Celsius):
temperature = np.array([18, 22, 19, 25, 31, 28, 15, 20, 33, 24])

# 1) Calcola media e deviazione standard delle temperature
# 2) Conta quanti giorni hanno superato i 25 gradi (senza usare un ciclo for!)
# 3) Crea un nuovo array con le temperature convertite in Fahrenheit: F = C * 9/5 + 32

# Scrivi qui sotto il tuo codice:
t = (temperature > 20)
print("t=",t)
print("t è",type(t))
print(t.sum())

temperature_F = temperature *9/5+32