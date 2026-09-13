"""
MODULO 4 - SCIKIT-LEARN
========================
Appunti pratici commentati sull'uso di scikit-learn per Machine Learning.

Prerequisiti: teoria di ML/statistical learning (bias-variance,
overfitting/underfitting, train/test, cross-validation, metriche, etc..).
Qui vediamo come questi concetti si traducono in codice con la libreria
principale del Machine Learning in Python.

Idea generale di scikit-learn:
- Ogni modello (o trasformazione) è un OGGETTO con la stessa interfaccia:
    .fit(X_train, y_train)       -> impara i parametri dai dati di training
    .predict(X_test)      -> genera previsioni su nuovi dati
    .transform(X)    -> trasforma i dati (es. scaling, encoding)
    .fit_transform(X)-> fit + transform in un colpo solo (usato sui dati di training)
- X è sempre una matrice 2D (n_campioni, n_feature), anche con una sola feature.
- y è un vettore 1D con i target (classi o valori numerici).

Questa uniformità è il punto di forza della libreria: una volta capito il
pattern fit/predict, si usa allo stesso modo per qualsiasi modello.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. DATASET DI ESEMPIO
# ---------------------------------------------------------------------------
# Usiamo un dataset già incluso in sklearn per concentrarci sui concetti
# senza perdere tempo nel caricamento dati (che so già fare con Pandas).
from sklearn.datasets import load_breast_cancer #importo la funzione

dati = load_breast_cancer() # qui sto caricando il dataset

###  dati non è un normale DataFrame Pandas: è un oggetto di sklearn che contiene diverse cose. Per esempio:
###dati.data, dati.target, dati.feature_names, etc...

## dati.data contiene le osservazioni (569 osservazioni e 30 features)
## ma senza i nomi delle colonne feature



X = pd.DataFrame(dati.data, columns=dati.feature_names)  # feature (30 colonne numeriche)
### lo faccio diventare un df di Pandas; con columns=... gli sto dicendo come chiamare le colonne

"""
Potevo anche lavorare direttamente con gli array di Numpy.
Si usano spesso DataFrame e Series perché sono più comodi da leggere e manipolare.

Con NumPy:
X[:, 3]

devi ricordarti cosa rappresenta la quarta colonna.

Con Pandas:

X["mean area"]
sai subito cosa stai prendendo.

Stessa cosa quando vuoi guardare i dati:

X.head()
X.describe()
X.columns

sono molto comodi.

Ma il modello funzionerebbe comunque con model.fit(X,y) con X e y numpy array.





"""





y = pd.Series(dati.target, name="target")  # 0 = maligno, 1 = benigno (classificazione binaria)
# è una series (praticamente una colonna, un vettore)




print("Shape X:", X.shape) #dimensioni di X (righe/colonne)
print("Distribuzione classi:\n", y.value_counts()) # per vedere quanti sample sono di una classe e dell'altra


# ---------------------------------------------------------------------------
# 2. TRAIN/TEST SPLIT
# ---------------------------------------------------------------------------
# Valutare un modello sugli stessi dati con cui è stato
# addestrato dà una stima ottimistica e inaffidabile delle sue performance
# (rischio di overfitting mascherato). Per questo si separano i dati in:
# - training set: per addestrare il modello
# - test set: per valutarlo su dati mai visti, simulando dati "nuovi"


from sklearn.model_selection import train_test_split


"""
X,y rappresentano il dataset totale dobbiamo suddividere noi le 569 osservazioni in training set e test set
"""



X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2,random_state=42,      # 20% dei dati al test set, 80% al training    # seed fisso: rende lo split riproducibile
    stratify=y           # con stratify=y mantengo le stesse proporzioni di classi in train e test
                          # (importante se le classi sono sbilanciate)
)
# Ovviamente imposto il seed cosi ogni volta che eseguo il codice lo split casuale sarà sempre uguale.

print("\nTrain:", X_train.shape, "Test:", X_test.shape)


# ---------------------------------------------------------------------------
# 3. PREPROCESSING: STANDARDIZZAZIONE
# ---------------------------------------------------------------------------
# Richiamo teorico: molti modelli (regressione logistica, SVM, KNN, reti
# neurali) sono sensibili alla scala delle feature: se una variabile va da
# 0 a 1 e un'altra da 0 a 10000, quella con range più ampio "domina"
# l'ottimizzazione. Gli alberi decisionali/random forest invece NON ne hanno
# bisogno, perché lavorano per soglie su singole feature.


# StandardScaler trasforma ogni feature in modo che abbia media 0 e
# deviazione standard 1: z = (x - media) / deviazione_standard
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler() #Crea un oggetto StandardScaler e lo chiama scaler

# IMPORTANTE: fit_transform SOLO sul training set. Il test set si trasforma
# con transform (usando media e deviazione standard calcolate sul training).
# Questo evita il "data leakage": il test set deve restare informazione
# mai vista, anche nelle statistiche di scaling.
X_train_scaled = scaler.fit_transform(X_train) #con fit calcolo media e std delle feature, con transform standardizzo
X_test_scaled = scaler.transform(X_test)

print("X_train_scaled ora è un numpy array")
print(type(X_train_scaled))
# Qui non ho più fit, scaler prende le medie e deviazioni standard che aveva già imparato da X_train e le usa per trasformare X_test
## La logica è:imparo la trasformazione sul training set e poi applico 
## esattamente quella trasformazione a qualunque dato futuro.


# ---------------------------------------------------------------------------
# 4. PRIMO MODELLO: REGRESSIONE LOGISTICA (classificazione)
# ---------------------------------------------------------------------------
# Richiamo: nonostante il nome, è un modello di
# classificazione. Stima la probabilità che un campione appartenga alla
# classe 1 tramite la funzione sigmoide applicata a una combinazione
# lineare delle feature. Se p >= 0.5 -> classe 1, altrimenti classe 0.
from sklearn.linear_model import LogisticRegression

modello_log = LogisticRegression(max_iter=10000)  # max_iter alto per garantire convergenza
modello_log.fit(X_train_scaled, y_train)  # addestramento: trova i coefficienti ottimali
#ora modello_log contiene gia i coefficienti ottimali

y_pred_log = modello_log.predict(X_test_scaled)  # qui gli do il test set
# e gli dico: "per ogni osservazione dimmi quale classe prevedi"
y_proba_log = modello_log.predict_proba(X_test_scaled) 
# Qui invece non vuoi solo la classe finale, ma vuoi sapere:
#  con che probabilità il modello assegna ogni osservazione a ciascuna classe


# ---------------------------------------------------------------------------
# 5. SECONDO MODELLO: RANDOM FOREST (classificazione)
# ---------------------------------------------------------------------------
# Richiamo teorico: è un insieme (ensemble) di molti alberi decisionali,
# ognuno addestrato su un sottoinsieme casuale di dati e feature (bagging).
# La previsione finale è la media/maggioranza dei singoli alberi: questo
# riduce la varianza rispetto a un singolo albero (che tende a overfittare).
# Non richiede scaling delle feature.
# riduce di molto la varianza rispetto a un singolo albero, che di solito tende all'overfitting
from sklearn.ensemble import RandomForestClassifier

modello_rf = RandomForestClassifier(
    n_estimators=200,   # numero di alberi nella foresta
    random_state=42
)
modello_rf.fit(X_train, y_train)  # nota: uso X_train NON scalato, non serve
y_pred_rf = modello_rf.predict(X_test)


# ---------------------------------------------------------------------------
# 6. METRICHE DI VALUTAZIONE (classificazione)
# ---------------------------------------------------------------------------
# Richiamo teorico rapido:
# - Accuracy: % di previsioni corrette. Fuorviante con classi sbilanciate
#   (es. 95% accuracy se il 95% dei dati è di una sola classe, anche
#   predicendo sempre quella classe).
# - Precision: tra i campioni predetti come classe 1, quanti lo sono
#   davvero (utile quando i falsi positivi sono costosi).
# - Recall: tra i campioni realmente di classe 1, quanti sono stati
#   trovati (utile quando i falsi negativi sono costosi, es. diagnosi).
# - F1-score: media armonica tra precision e recall, buon compromesso
#   quando servono entrambe.
# - Confusion matrix: tabella con veri positivi/negativi e falsi
#   positivi/negativi, la base per calcolare tutte le metriche sopra.
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

print("\n--- Regressione Logistica ---")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Precision:", precision_score(y_test, y_pred_log))
print("Recall:", recall_score(y_test, y_pred_log))
print("F1:", f1_score(y_test, y_pred_log))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred_log))

print("\n--- Random Forest ---")
print(classification_report(y_test, y_pred_rf))  # riassume precision/recall/f1 per classe



# ---------------------------------------------------------------------------
# 7. CROSS-VALIDATION
# ---------------------------------------------------------------------------
# Richiamo teorico: un singolo train/test split dà una stima delle
# performance che dipende dal caso (quali campioni sono finiti nel test).
# La k-fold cross-validation divide il training set in k parti (fold):
# si allena k volte, ogni volta usando k-1 fold per training e 1 fold per
# validazione, ruotando il fold di validazione. Il risultato è una stima
# più robusta e la sua deviazione standard indica quanto è stabile.


from sklearn.model_selection import cross_val_score

punteggi = cross_val_score(
    LogisticRegression(max_iter=10000),
    X, y,           # qui si usa tutto il dataset: la CV gestisce da sola gli split
    cv=5,           # 5-fold cross-validation
    scoring="f1"    # metrica da calcolare su ogni fold
)
print("\nF1 per fold:", punteggi)
print("F1 medio:", punteggi.mean(), "+/-", punteggi.std())






"""
Questa singola istruzione fa parecchie cose.

LogisticRegression(max_iter=10000) crea ogni volta il modello di regressione logistica da addestrare.

X, y sono rispettivamente tutte le feature e tutti i target.

Con cv=5 gli dici di fare una 5-fold cross-validation.

Quindi le 569 osservazioni vengono suddivise grossomodo in 5 gruppi:

Fold 1
Fold 2
Fold 3
Fold 4
Fold 5

e sklearn fa automaticamente:

Giro 1: train = 2,3,4,5    validation = 1
Giro 2: train = 1,3,4,5    validation = 2
Giro 3: train = 1,2,4,5    validation = 3
Giro 4: train = 1,2,3,5    validation = 4
Giro 5: train = 1,2,3,4    validation = 5

Quindi il modello viene addestrato 5 volte da zero.

Poi: scoring="f1"

dice a sklearn:

    per ogni giro, valuta il modello usando l'F1-score.

Perciò: punteggi sarà un array NumPy con 5 numeri, per esempio:

array([0.96, 0.98, 0.97, 0.95, 0.98])

Uno per ogni fold.
"""

### Importante!!!
"""
Osservazione importante: 

Qui c'è un imprecisione perche' i dati dovrebbero esssere scalati invece io gli passo l'X originario non scalato

Ma se creo X_scaled con fit_transform su tutto X e poi lo passo 
alla cross-validation, si ha  un problema anche peggiore: il data leakage. Infatti:
  
La media e la deviazione standard usate per scalare sono calcolate anche sui dati che, fold per fold,
finiranno nella parte di validazione. In pratica il modello "sbircia" informazioni statistiche 
 (seppur minime) provenienti da dati che dovrebbe trattare come mai visti.

"""


"""
La soluzione corretta è usare una Pipeline dentro la cross-validation,
 esattamente il concetto introdotto al punto 8 ma applicato qui, il codice diventerebbe:

from sklearn.pipeline import Pipeline

pipeline_log = Pipeline([
    ("scaler", StandardScaler()),
    ("modello", LogisticRegression(max_iter=1000))
])

punteggi = cross_val_score(pipeline_log, X, y, cv=5, scoring="f1")

"""






# ---------------------------------------------------------------------------
# 8. PIPELINE: preprocessing + modello in un unico oggetto
# ---------------------------------------------------------------------------
# Una Pipeline incatena più step (es. scaler poi
# modello) in un solo oggetto con interfaccia fit/predict. Vantaggi:
# - evita data leakage automaticamente (lo scaler viene "fittato" solo sul
#   training set anche dentro la cross-validation)
# - codice più pulito e riutilizzabile
# - utile soprattutto quando si fa hyperparameter tuning (sotto)



from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("modello", LogisticRegression(max_iter=10000))
])
pipeline.fit(X_train, y_train)  
print("\nAccuracy pipeline:", pipeline.score(X_test, y_test))  # .score = accuracy per i classificatori



"""
sto dicendo:
prima applica StandardScaler, poi passa il risultato alla LogisticRegression.

La sintassi è una lista di tuple:
[
    ("nome_step_1", oggetto_step_1),
    ("nome_step_2", oggetto_step_2)
]

Quindi qui: ("scaler", StandardScaler()) è il primo step, mentre: ("modello", LogisticRegression(...))
è il secondo.

I nomi "scaler" e "modello" li scegli tu: servono per poter recuperare facilmente 
i vari pezzi della pipeline in seguito.

La cosa ancora più comoda arriva quando fai una previsione. Per esempio:
potevo aggiungere y_pred = pipeline.predict(X_test)

non devi fare manualmente
X_test_scaled = scaler.transform(X_test)
modello.predict(X_test_scaled)
La pipeline fa tutto automaticamente
Nota importantissima: sul test non rifà il fit dello scaler. Usa media e deviazione standard 
imparate durante pipeline.fit(X_train, y_train).
Infatti noi usiamo pipeline.score(X_test,y_test):
Questo applica il preprocessing già imparato ai nuovi dati + usa il modello per predire i sample
e sputa fuori lo score di default del modello (in questo caso per la Logistic regression l' Accuracy)

Quindi mantiene esattamente la logica vista prima.

In più, come abbiamo visto prima, è fondamentale nella cross-validation, per evitare data leakage
"""





# ---------------------------------------------------------------------------
# 9. HYPERPARAMETER TUNING CON GRIDSEARCHCV
# ---------------------------------------------------------------------------
# Richiamo teorico: gli iperparametri (es. n_estimators, max_depth) non si
# imparano dai dati come i parametri del modello, vanno scelti a priori.
# GridSearchCV prova tutte le combinazioni di una griglia di valori,
# valutando ciascuna con cross-validation, e restituisce la combinazione
# migliore. Costoso computazionalmente ma sistematico.
from sklearn.model_selection import GridSearchCV

griglia = {
    "n_estimators": [100, 200],
    "max_depth": [None, 5, 10]  # None = alberi senza limite di profondità (rischio overfitting)
}                       #Gli do varie possibilità e lui prova tutte le combo tra n_est e max_depth
              ### ----> in totale ho 6 combinazioni possibili prodotte dalla griglia.
ricerca = GridSearchCV(
    RandomForestClassifier(random_state=42), #random_state=42 qui serve perché il Random Forest ha della casualità interna: campionamento dei dati, scelta delle feature ecc. Fissandolo, rendi i risultati riproducibili.
    param_grid=griglia,
    cv=3,
    scoring="f1"
)
ricerca.fit(X_train, y_train)

print("\nMigliori parametri:", ricerca.best_params_)
print("Miglior F1 in CV:", ricerca.best_score_)

# il modello migliore è già pronto all'uso:
miglior_modello = ricerca.best_estimator_

""" In una frase gli sto dicendo:
"Prova 6 Random Forest diversi, valuta ciascuno con 3-fold CV usando l'F1 e dammi quello che mediamente funziona meglio."

ricerca.best_params_
ti restituisce gli iperparametri migliori.

Per esempio potrebbe uscire:

{
    "max_depth": 5,
    "n_estimators": 200
}

Significa che tra quelle che hai provato, la configurazione migliore è stata:

RandomForestClassifier(
    n_estimators=200,
    max_depth=5
)


"""

# ---------------------------------------------------------------------------
# 10. ESEMPIO DI REGRESSIONE (target numerico, non classi)
# ---------------------------------------------------------------------------
# Richiamo teorico: nella regressione il target è continuo (es. prezzo,
# temperatura). Le metriche cambiano di conseguenza:
# - MAE (Mean Absolute Error): errore medio in valore assoluto, stessa
#   unità di misura del target, facile da interpretare.
# - MSE (Mean Squared Error): penalizza di più gli errori grandi (perché
#   eleva al quadrato); RMSE è la sua radice quadrata, torna nell'unità
#   di misura originale.
# - R^2: quota di varianza del target spiegata dal modello (1 = perfetto,
#   0 = come predire sempre la media, può essere negativo se il modello
#   è peggio della media).
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

dati_case = fetch_california_housing()
X_reg = pd.DataFrame(dati_case.data, columns=dati_case.feature_names)
y_reg = pd.Series(dati_case.target, name="prezzo_medio")

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

modello_lineare = LinearRegression()
modello_lineare.fit(X_reg_train, y_reg_train)
y_reg_pred = modello_lineare.predict(X_reg_test)

print("\n--- Regressione lineare (California housing) ---")
print("MAE:", mean_absolute_error(y_reg_test, y_reg_pred))
print("RMSE:", mean_squared_error(y_reg_test, y_reg_pred) ** 0.5)
print("R2:", r2_score(y_reg_test, y_reg_pred))


"""NOTE: qui non abbiamo standardizzato

   Una buona regola pratica è:

LinearRegression semplice → scaling opzionale
Ridge / Lasso / ElasticNet → scaling praticamente obbligatorio
KNN / SVM / regressione logistica → scaling spesso importante
Decision Tree / Random Forest → scaling inutile

E normalmente non standardizzi y nella regression, quindi:

y_reg_train
y_reg_test

restano nella loro unità originale. Così anche errori comeMAE e RMSE 
rimangono immediatamente interpretabili nell'unità originale di y.
"""




# ---------------------------------------------------------------------------
# RIEPILOGO / PROMEMORIA
# ---------------------------------------------------------------------------
# - fit su training, transform/predict anche su test; MAI fit sul test set.
# - scaling utile per modelli lineari/basati su distanza, inutile per alberi.
# - accuracy da sola non basta quasi mai: guardare precision/recall/F1,
#   soprattutto con classi sbilanciate.
# - cross_val_score / GridSearchCV danno stime più robuste di un singolo split.
# - Pipeline = buona pratica per evitare data leakage e tenere il codice ordinato.
# - classificazione -> target discreto (classi); regressione -> target continuo:
#   metriche e modelli diversi, ma stessa logica fit/predict di sklearn.
