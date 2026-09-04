import pandas as pd

df = pd.DataFrame({
    "prodotto": ["A", "B", "C", "D", "E"],
    "prezzo": [10, 25, 15, 40, 8],
    "unita_vendute": [100, 30, 80, 12, 200],
})

# Selezione colonna
print("--- Colonna prezzo ---")
print(df["prezzo"])

# Filtro (condizione booleana, come in matematica: {x : prezzo(x) > 15})
print("\n--- Solo prodotti con prezzo > 15 ---")
print(df[df["prezzo"] > 15])

# Nuova colonna calcolata
df["ricavo"] = df["prezzo"] * df["unita_vendute"]
print("\n--- Con colonna ricavo ---")
print(df)

# Ordinamento
print("\n--- Ordinato per ricavo decrescente ---")
print(df.sort_values("ricavo", ascending=False))

# Statistiche descrittive rapide
print("\n--- Statistiche descrittive ---")
print(df[["prezzo", "unita_vendute", "ricavo"]].describe())
