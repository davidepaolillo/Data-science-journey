# Lista: ordinata, modificabile, con duplicati
numeri = [3, 1, 4, 1, 5, 9]
numeri.append(2)
print("Lista:", numeri)
print("Elemento indice 2:", numeri[2])
print("Slice [1:4]:", numeri[1:4])

# Tupla: ordinata, IMMUTABILE (utile per dati che non devono cambiare)
punto = (3.5, 7.2)
print("Tupla:", punto)

# Dizionario: coppie chiave-valore (fondamentale per JSON/dati strutturati)
persona = {"nome": "Marco", "eta": 28, "citta": "Milano"}
print("Dizionario:", persona)
print("Nome:", persona["nome"])

# Set: elementi unici, non ordinati
unici = set(numeri)
print("Set (duplicati rimossi):", unici)

# List comprehension: la sintassi più usata in DS per trasformare/filtrare dati
quadrati_pari = [x**2 for x in numeri if x % 2 == 0]
print("Quadrati dei numeri pari:", quadrati_pari)
