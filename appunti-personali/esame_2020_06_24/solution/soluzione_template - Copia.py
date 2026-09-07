# -*- coding: utf-8 -*-
"""
Esame di Programmazione 1 - Appello del 20 giugno 2020

COGNOME:    XXXXX
NOME:       XXXXX
MATRICOLA:  XXXXX
POSTAZIONE: XXXXX
"""

from pairslist import *
from math import sqrt


# Esercizio 1
def Norma(x, t):
    if t == 0:
        return Max(Map(Abs,x))
    if t==1:
        return Sum(Map(Abs,x))
    if t == 2:
        return Sum(Map(lambda y : y**2,x))
    
    return 0

# Esercizio 2
def Integrale(F, a, b, dx): 
    def somma(F,a,Next,b):
        if a > b:
            return 0
        return F(a) + somma(F,Next(a),Next,b)
    def Adddx(x):
    
        return x + dx
    
    return dx*somma(F,a+dx/2,Adddx,b)


# Esercizio 3: Merge Sort with pairslist
def MergeSort(Ls, Cmp=lambda x,y: x<y):
    return Ls


# Esercizio 4: 
class Region(object):
    def __init__(self, row):
        self.Data=row[0]
        self.Nome=row[3]
        self.TerapiaIntensiva=int(row[7])
        self.NuoviPositivi=int(row[12])
        self.Deceduti=int(row[14])
        self.Totale=int(row[15])
        self.Tamponi=int(row[16])
        
    def __str__(self):
        return 'Regione:{},Totale:{},Deceduti:{},Tamponi:{}'.format(self.Nome,self.Totale,self.Deceduti,self.Tamponi)
    def __lt__(self,other):
        if self.Deceduti < self.Totale:
            return True
        return False
    # Esercizio 5:        
    
    # Esercizio 6:


# Esercizio 7:
def Parse(filename):
    Ls = []
    
    fh= open(filename,'r',encoding='utf-8')
    fh.readline()
    for line in fh:
        row= line.replace('\n','').split(',')
        Ls.append(Region(row))
        
    return Ls


# Esercizio 8 
"""(Punti 3) Si scriva una funzione TopRegion(Ls, n=5), che prende in input una lista di oggetti
di tipo Region come restituiti dalla funzione Parse, e che restituisce le prime n regioni con il
maggior rapporto tra numeri di morti e pazienti infetti."""
def TopRegion(Ls, n=3):
    return sorted(Ls,reverse = True)[:n]

# Esercizio 9
"""(Punti 3) Si scriva una funzione ParseFiles(names) che prende in input una lista di nomi di
files che devono essere letti. La funzione per ogni nome della lista, deve richiamare la funzione
Parse, leggere il contenuto del file ottenendo una lista di oggetti di tipo Region, e deve restituire
alla fine la lista complessiva di oggetti letti dai file di input.
Nella funzione di test, si chiede di leggere cinque file, dello stesso tipo del file .csv descritto
sopra, ma che si riferiscono a date diverse."""

def ParseFiles(names):
    Ls=[]
    for file in names:
        Bs=Parse(file)
        Ls.append(Bs)
    return Ls
    
    
        
   

# Esercizio 10
"""(Punti 5) Si scrive una funzione ComputeAverage(Ls), che prende in input una lista di oggetti
di tipo Region, letti per esempio con la funzione ParseFiles(names), e calcola, per ogni regione,
la media aritmetica giornaliera dei nuovi casi registrati. La funzione deve restituire un dizionario
con una chiave per ogni regione, a cui corrisponde come valore la media giornaliera calcolata di
nuovi casi."""

def ComputeAverage(Ls):
    D ={}
    diz={}
    for x in Ls:
        D[x.Nome] = 1 + D.get(x.Nome,0)
        

    return D


#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":
    # Esercizio 1
    from random import seed, randint
    seed(23)
    x = MakeRandomInts(10, 0, 100)
    print(Norma(x,0))
    print(Norma(x,1))
    print(Norma(x,2))
    
    # Esercizio 2
    def Cubo(x):
        return x*x*x
    print(Integrale(Cubo, 0, 1, 0.05))


    # Esercizio 3
    print("===>>> Test Esercizio 3:")

    from random import seed
    # Inizializza il generatore di numeri casuali
    seed(13)
    Ls = MakeRandomInts(10, 0, 100)
    print(Ls)
    print('List ordinata in modo decrescente:', MergeSort(Ls, lambda x,y: x > y))

    print()

    # Esercizio 7
    print("===>>> Test Esercizio 7:")
    Ls = Parse('dpc-covid19-ita-regioni-latest.csv')
    for reg in Ls[:3]:
        print(reg)
    print()
    
    
    # Esercizio 8
    print("===>>> Test Esercizio 8:")
    for p in TopRegion(Ls):
        print(p.Nome, p.Deceduti/p.Totale)
    print()

    # Esercizio 9
    print("===>>> Test Esercizio 9:")
    Fs = ['dpc-covid19-ita-regioni-20200614.csv',
          'dpc-covid19-ita-regioni-20200615.csv',
          'dpc-covid19-ita-regioni-20200616.csv',
          'dpc-covid19-ita-regioni-20200617.csv',
          'dpc-covid19-ita-regioni-20200618.csv',
          'dpc-covid19-ita-regioni-20200619.csv',
          'dpc-covid19-ita-regioni-20200620.csv']
    As = ParseFiles(Fs)
    print(As[:5])
    print()
    
    # Esercizio 10
    print("===>>> Test Esercizio 10:")
    Bs = ComputeAverage(As)
    try:
        print(Bs['Lombardia'])
        print(Bs['Piemonte'])
        print(Bs['Veneto'])
    except:
        print('Errore nella soluzione di ComputeAverage')