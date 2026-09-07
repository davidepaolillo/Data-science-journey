import pandas as pd

dati = [
    {"categoria": "A", "valore": 10},
    {"categoria": "B", "valore": 20},
    {"categoria": "A", "valore": 30},
    {"categoria": "B", "valore": 5},
]

# Creo la DataFrame (tabella) dalla lista di dizionari
df = pd.DataFrame(dati)
print("--- DataFrame originale ---")
print(df)
print()

print("--- Info sulla struttura ---")
print(df.info())
print()

# Questa riga fa TUTTO quello che hai scritto a mano prima
medie = df.groupby("categoria")["valore"].mean()
print("--- Medie per categoria ---")
print(medie)
