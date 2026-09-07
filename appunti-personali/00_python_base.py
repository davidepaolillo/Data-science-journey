# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:34:26 2021

@author: lilpao
"""
# predicato che restituisce true se la stringa è ordinata alfabeticamente se noi false
def Is_abcderian(string):
    previous=string[0]
    for item in string:
        if item < previous:
            return False
        previous= item
    return True
        
        

# ora con la ricorsione
# la funzione continua a richiam se stessa finche non si rientra in un base case 
# ad ogni chiamata però cambia l argomento di imput, in questo caso ad ogni chiamata la f.ne non passerà la stringa originaria
# ma una stringa via via piu corta

def recIs_abcderian(string):   
    if len(string) <= 1:     # BASE CASE A
        return True
    if string[0]>string[1]:  # BASE CASE B (analizzo via via all interno della stringa passata il primo e il secondo elemento)
        return False
    return recIs_abcderian(string[1:])

# ad es con 'abcd' non rientro in un base case allora passa a 'cd' anche qui non raggiungo un base case allora passa 
# a 'd'. A questo punto sono nel base case A e restituisce True dopo aver analizzato tutti gli altri.


a='parola'
print(a.upper()) # questo METODO mi da la stringa in maiuscol
                    # se a fosse stato = 3 avrei avuto un errore del tipo 'int' object has no attribute upper
                    # a è una variabile , ogni variabile '' al suo interno '' ha un OGGETTO (int,float,str,....)
                    # i metodi sono funzioni associate a dei tipi di dati precisi

# ovviamente posso assegnare un nuovo valore ad una variabile 

# gli operatori di * + oltre a fare i conti se applicati a degli interi, si possono usare anche su altri oggetti 
# ad esempio stringhe tuple e liste
print('prog'+'1')
print('2'* 20) 
As=[1,2,3,4]    
Bs=[5,6,7,8]  # il meno tra due liste invece non ha senso
print(As*2)
print (As+Bs) # è come append


# posso convertire oggetti in oggetti di altro tipo, ad esempio int e float sono funzioni che trasformano stringhe numeriche in oggetti di tipo int/float

# LISTE E DIZIONARI
a=[1,22,34]
for l in a :
    print (l)
    
# metodo piu import nelle liste è l'append
As.append(2)
As.append('pippo')# posso concatenare anche liste e stringhe ( ma non con il + )
print(As)

print('se voglio togliere un elemento modificando la lista posso usare la parola chiave del')
A=[3,6,9,12]
del(A[1]) # in questo modo ho modificato la lista !!!
print(A)

# se voglio indicizzare gli elementi posso usare enumerate
# ritorna delle tuple ( sono come le liste ma con le tonde e NON SONO MODIFICABILI) 
# con la posizione e l'elemento corrisp.te a quella posiz.ne
X=[3,1,7,8,9]   
for x in enumerate(X):
    print(x)

for pos,x in enumerate(X): # cosi prendo solo i valori
    print(x)

for pos,x in enumerate(X):
    print(f'{pos} = {x}')  # fstring

print('funzione sorted e metodo .sort')
for y in sorted(X):
    print(y)
   
print(X)     # la cosa imp.te è che il metodo .sort mi modifica mia lista mentre sorted no
X.sort()
print(X)

# la funzione sorted puo essere usata anche con una key ovvero una funzione e specificando in che ordine si vuole 
# ordinare la lista (reverse=True decrescente)  sorted(Ls,key,reverse=True)
R=[1,2,3,-1,-5,-9999,2222,30000]

C=sorted(R,key=lambda x:x*x, reverse=True)  

print(C)  ## in questo caso sorted applica prima la funzione key a ogni elemento della lista ordina questa nuova lista(in base al reverse), e poi mi torna la lista 
          ## di partenza ordinata in base agli elementi che corrispondono all altra (  non è come fare sorted(map(C)) )
print('\n\n\nora dizionariniii')
print('\n\n')

# un dizionario è un oggetto di python che associa ad una CHIAVE un VALORE
# !!! posso attribuire ad una key anche una lista una stringa o anche un altro dizionario come valore
# senza alcun limite (es. degli alcolici dizionario di dizionari ) ma una chiave puo assumere solo dati base(stringhe oppure numeri)

# vediamo un esempio easy di Dizionario
d={}
d['key1'] = 1 
d['pippo'] = 'pluto'
d['valori'] = [12,35]

print(d)

# anche i dict si possono modificare ad es posso togliere una chiave e il suo elem corrisp.te  facendo cosi:

del d['key1']
print(d)

print('\n')

# se invece itero con un ciclo for su un dict python mi itera sulle chiavi
for x in d:
    print(x)

print('\n')

# se voglio invece solo i valori:
for x in d:
    print(d[x])
    
print('\n')
# posso usare una fstring? Alla grande
for x in d:
    print(f'{x} ==> {d[x]}')

print('\n')

# è interessante invce il metodo .items che unito al ciclo for mi dà anche qui le coppie chiave-valore

for x in d.items():
    print(x)
# se voglio una lista con queste coppie
print(list(d.items()))

# altri metodi per i dizionari:
#len(d): restituisce il numero di elementi nel dizionario d
#d.keys(): restituisce una lista (vista) delle chiavi del dizionario d
#d.values(): restituisce una lista (vista) dei valori del dizionario d
#key in d: restituisce True se la chiave key è nel dizionario d
#d.get(key, value): restituisce d[key] se key è in d, altrimenti restituisce il valore value

# importante: i dict sono strutture dati non ordinate, se un dizionario ha le stesse coppie k-v anche se in
# ordine diverso allora sono diversi

# posso usare la funzione sorted per i dizionari anche: la funzione sorted in generale RESTITUISCE UNA LISTA
# quindi se passo un dict a sorted mi da una lista con le chiavi ordinate in base al tipo di dato (stringhe, int, ecc..) 
# e alla key che ci metto
print('\n')
print('funzione sorted per dizionari')
dizionario={l:i for i,l in enumerate(R)} # <---- comprehension per dizionari
print(dizionario) 
print(sorted(dizionario))
print(sorted(dizionario,key= lambda x: x*x))
# IMPORTANTISSIMO PER ESAME: spesso devo ordinare le chiavi in base al valore associato alla chiave stessa
print(sorted(dizionario,key= lambda k : dizionario[k]))

# OSS. se le chiavi sono delle stringhe sorted(dict) mi da la lista delle chiavi ordinate in base all ordine alfabetico(inglese) che è l'ordinamento dell'inglese 
#      se le chiavi sono stringhe di numeri posso usare come key la funzione nativa int se voglio l ordinamento numerico
print('\n')
ddd={'1':19,'13':23,'8':7,'50':2,'79':11}
print(ddd)
print(sorted(ddd))
print(sorted(ddd,key=int))


print('\n\n ora stringhe e metodi importanti')
## vediamo ora qualcosa sulle stringhe
## le stringhe sono IMMUTABILI: (come le tuple) non si puo' cambiare il valore degli elementi al loro interno
## con appoaiti metodi , ma dobbiamo assegnare il valore nuovo della variabile.
# quindi str e tuple non sono modificabili, liste si
stringa='1 2 3 4'
stringaaa='1::2::3 4....'
## voglio fare una lista con gli elementi di questa stringa -----> metodo .split
print(stringa.split(' ')) 
print(stringaaa.split('::'))
 ## e se io volessi fare la stessa cosa ma nella stringa ci sono un numero indefinito di spazi? 
 ## come fasccio a ripulire gli spazi creando uuna lista con solo i numeri?
stringabrutta='1   2      3 4                     5'
# posso usare replace ma in questo caso dovrò apllicarlo piu volte
print(stringabrutta.replace('  ',''))
# la stringa si è accorciata ma non è ancora aposto, dovrò applicare ancora replace qualche volta ( e poi splittare se voglio la lista )
# per farlo posso scrivere una funzione ricorsiva
def pulizia(testo):
    if '  ' not in testo:  #LA PRIMA RIGA DELLE F.NI RICORSIVE è SEMPRE LA CONDIZIONE DI ARRESTO
        return testo      #CIOE CIO CHE PERMETTE AL PROGR DI NON ENTRARE IN UN LOOP INFINITO. ESSA CORRISPONDE ALLA CONDIZ PIU SEMPLICE,CIOE QUANDO NON DEVO FARE NIENTE( IN QUESTO CASO INFATTI SE NON SONO PRESENTI DOPPI SPAZI LA STRINGA è GIA A POSTO)
    else:
        testo=testo.replace('  ',' ')  # PULISCO LA STRINGA MA NON BASTA UNA VOLTA QUINDI LA FUNZIONE RICHIAMA SE STESSA FINCHE APPUNTO NON CI SON DOPPI SPAZI
        return pulizia(testo)
print(pulizia(stringabrutta).split(' '))

## da segnalare i metodi per stringhe .isalpha() e .isdigit()
print('\n\n piccolo accenno sui set')
# un altro tipo di dato ( che a lezione non abbiamo fatto sono i set). Sono simili ai dizionari perche si indicano
# le graffe. La cosa importante è che non hanno un ordine degli elementi e che non possono contenere elementi doppi
insieme=set()
lista=[1,2,3,3,4,7,-3,0,11,4,2,0,11,3,1]
for x in lista:
    insieme.add(x)
print(insieme)
# notiamo che ha rimosso tutti i duplicati e mi ha svaccato l ordine 
# ATTENZIONE: i set SONO iterabili, quindi sono utilissimi per tante cose
# ad esempio per rimuovere duplicati da una lista
listanoduplic = [x for x in insieme]
print(listanoduplic)
# poi la ordino 
listanoduplic2=sorted(listanoduplic,reverse=True) # se facevo sorted senza il reverse me la ordinava nell altro senso
print(listanoduplic2)