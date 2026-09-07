dati = [
    {"categoria": "A", "valore": 10},
    {"categoria": "B", "valore": 20},
    {"categoria": "A", "valore": 30},
    {"categoria": "B", "valore": 5},
]

somme = {}
conteggi = {}

for riga in dati:
    cat = riga["categoria"]
    val = riga["valore"]
    somme[cat] = somme.get(cat, 0) + val
    conteggi[cat] = conteggi.get(cat, 0) + 1

# --- la tua soluzione, con indentazione corretta ---
d = {}
for key in somme:
    d[key] = somme[key] / conteggi[key]

print("Medie per categoria:", d)
