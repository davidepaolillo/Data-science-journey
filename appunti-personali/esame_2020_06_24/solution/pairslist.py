# -*- coding: utf-8 -*-
"""
Costruttori e selettori di liste come sequenze di coppie

@author: gualandi
"""

# Versione della libreria
__version__ = '0.3.0'

# Lista delle funzioni che voglio esportare
__all__ = [
    'EmptyList', 'MakeList', 'Head', 'Tail', 'IsEmptyList',
    'PrintList', 'MakeRandomInts', 'Append', 'Length'
]



def EmptyList():
    """ Simbolo usato per indicare una lista vuota """
    return 'EL'

def MakeList(x, y=EmptyList()):
    """ Restituisce una lista come sequenza di coppie """
    return (x, y)

def Head(As):
    """ Restituisce il primo elemento della lista As """
    return As[0]

def Tail(As):
    """ Restituisce il secondo elemento della lista As """
    return As[1]

def PrintList(As):
    """ Pretty print for a list of elements """
    def PrintListI(As):
        if not IsEmptyList(As):
            print(Head(As), end='')
            if not IsEmptyList(Tail(As)):            
                print(', ', end='')
            PrintListI(Tail(As))
    print('{', end='')
    PrintListI(As)
    print('}')    

def IsEmptyList(As):
    """ Controlla se As è una lista vuota """
    return As == EmptyList()

# Inizializza il generatore di numeri casuali
# Vedi la documentazione del modulo random:
# https://docs.python.org/3/library/random.html
from random import randint, seed
seed(13)
    
def MakeRandomInts(n, a, b):
    """ Restituisce una lista n di numeri causali, uniformente distribuiti
        nell'intervallo [a,b] (estremi compresi) """
    if n == 0:
        return EmptyList()
    return MakeList(randint(a,b), MakeRandomInts(n-1, a, b))


def Append(As, Bs):
    """ Crea una nuova lista, con prima la sequenza di elementi di As,
        poi la sequenza di elementi di Bs """

    if IsEmptyList(As):
        return Bs

    return MakeList(Head(As), Append(Tail(As), Bs))

def Length(Ls):
    """ Calcola la lunghezza della lista (modo iterativo, ciclo while) """
    n = 0
    As = Ls
    while not IsEmptyList(As):
        n = n + 1
        As = Tail(As)
    return n