"""
Created on Fri Sep 11 22:57:48 2026

@author: lilpao
"""

import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import is_numeric_dtype

import os

os.chdir(r"C:\Users\lilpao\OneDrive\Desktop\Data-science-journey\progetto-house-pricing")
print(os.getcwd())

"""
STEP 1: Carcicamento dei dati e prima analisi esplorativa
"""
df = pd.read_csv("train.csv")
visual=df.head()
print(visual)

print('\n dimensioni del dataset')
print(df.shape)

print(df.describe())

df1 = pd.read_csv("test.csv")
print(df1.shape)

print(df.info())

#analizzo la variabile target (house price)

print("\n variabile target")
print(df["SalePrice"].describe())
sns.histplot(df["SalePrice"],kde="True")
plt.show()
plt.close()
# La distribuzione di SalePrice è chiaramente asimmetrica (skewed a destra). Lo vedi sia dal grafico (la "coda" lunga verso destra, pochi valori molto alti) sia dai numeri:

# media 180921 > mediana (50%) 163.000. il max (755000) è molto più lontano dal 75° percentile (214000) rispetto a quanto il min (34900) lo sia dal 25° percentile (129975) — asimmetria anche qui

""" STEP 2 - Sistemo i valori mancanti
lavoro su colonne con valori nulli (NaN)
df.isnull() restituisce un nuovo DataFrame della stessa forma di df (stesse righe, stesse colonne)
ma pieno di valori booleani: True dove la cella è mancante (NaN), False dove c è un valore
.sum() applicata a un df somma per colonna quindi ottengo series di 80 righe, con nome colonna e numero di
NaN in quella colonna. Poi filtro tenendo solo quelle che hanno almeno un valore mancante
"""
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
print(missing)


"""" RULE: Su una Series for x in missing: itera sui valori. Se invece fai:
for col in missing.index: itera sugli indici (nomi delle colonne)
Se voglio entrambe le cose:for col, value in missing.items()
Su un DataFrame, invece: for x in df: itera sui nomi delle colonne, non sulle righe."""


for c in missing.index:

    if is_numeric_dtype(df[c]):
        print(c, "-> NUMERICA -> mediana")

    else:
        print(c, "-> CATEGORICA -> None")


for col in missing.index :
    if df[col].dtype == "object": #dtype in pandas ti dice che tipo di dati contiene una series
        df[col] = df[col].fillna("None")
    else:
        df[col] = df[col].fillna(df[col].median()) #sotituisco i NaN delle solo variabili numeriche
        # Uso la mediana al posto della media perche è meno sensibile agli outlier
   

### print(df.isnull().sum().sum())  # somma totale dei missing rimasti: da 0 --> ha funzionato

"""
STEP 3 - Encoding delle variabili categoriche 
"""
colonne_categoriche = list(df.select_dtypes(include="object").columns)

print("\n colonne categoriche", colonne_categoriche)
print(type(colonne_categoriche))

df_encoded = pd.get_dummies(df, columns=colonne_categoriche,drop_first=True) #questa riga fa il one-hot-encoding
#drop first = True elimina una colonna per ogni dummy variable categorica. La prima diventa colonna di riferimento (se le altre sono tutte =0 significa che è quella categoria lì)
print(df_encoded.shape)


"""
STEP 4 - Split dei dati in training set e test set
"""
X = df_encoded.drop(columns=["SalePrice", "Id"])  # tutte le feature, tolti target e Id (che non è predittivo)
y = df_encoded["SalePrice"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape)

"""
STEP 5 - Training a first baseline model (linear regression)
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

pipeline_baseline = Pipeline([
    ("scaler", StandardScaler()),
    ("modello", LinearRegression())
])

pipeline_baseline.fit(X_train, y_train)
y_pred = pipeline_baseline.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)
print("R2:", r2_score(y_test, y_pred))


"""
STEP 6 - Errori altissimi, probabilmente dovuti al numero elevato di feature rispetto ai dati

Provo a regolarizzare con Lasso, poiche magari molte feature (soprattutto le dummies) non servono
"""

from sklearn.linear_model import Lasso

pipeline_lasso = Pipeline([
    ("scaler", StandardScaler()),
    ("modello", Lasso(alpha=1000, max_iter=10000))  # alpha da tarare, max_iter alto per sicurezza di convergenza
])

pipeline_lasso.fit(X_train, y_train)
y_pred_lasso = pipeline_lasso.predict(X_test)

print("\n Lasso")
print("MAE:", mean_absolute_error(y_test, y_pred_lasso))
print("RMSE:", mean_squared_error(y_test, y_pred_lasso) ** 0.5)
print("R2:", r2_score(y_test, y_pred_lasso))



coefficienti = pipeline_lasso.named_steps["modello"].coef_ #accedo all'oggetto "Lasso" della pipeline
print("Feature azzerate:", (coefficienti == 0).sum(), "su", len(coefficienti))

"""
STEP 7 - Tuning alpha: non possiamo scegliere alpha in base alla performance sul test set perche commetteremmo un errore concettuale 
    Quindi cerchiamo di otttimizzare con GridSearch
"""


from sklearn.model_selection import GridSearchCV
import numpy as np

pipeline_lasso = Pipeline([
    ("scaler", StandardScaler()),
    ("modello", Lasso(max_iter=100000))
])

griglia = {
    "modello__alpha": [10, 50, 100, 300, 500, 1000, 1500, 2000, 2500, 3000] # notare il doppio underscore!
}

ricerca = GridSearchCV(
    pipeline_lasso,
    param_grid=griglia,
    cv=5,
    scoring="neg_mean_squared_error"  # sklearn richiede metriche da MASSIMIZZARE, quindi l'MSE va messo negativo
)

ricerca.fit(X_train, y_train)

print("Miglior alpha:", ricerca.best_params_)
print("Miglior RMSE in CV:", (-ricerca.best_score_) ** 0.5)

miglior_modello = ricerca.best_estimator_
y_pred_finale = miglior_modello.predict(X_test)
print("R2 test:", r2_score(y_test, y_pred_finale))

"""
STEP 8: con dati skewed, le case molto costose hanno valori enormi e differenze assolute enormi anche con piccoli errori percentuali. Il modello, per minimizzare l'errore quadratico totale, tende a concentrarsi eccessivamente sul far bene sulle case costose (perché lì gli errori assoluti — e quindi quadratici — pesano di più), sacrificando un po' di precisione sulle case "normali", che sono la maggioranza.
rende la distribuzione del target più simmetrica/vicina a una gaussiana — condizione che i modelli lineari "preferiscono" per lavorare bene. 
"""
print("\n after log scaling the target variable" )
y_log = np.log1p(y) #equivale a log(1+y)

X_train, X_test, y_train_log, y_test_log = train_test_split(X, y_log, test_size=0.2, random_state=42)




griglia_log = {
    "modello__alpha": [0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]
}

ricerca_log = GridSearchCV(
    Pipeline([
        ("scaler", StandardScaler()),
        ("modello", Lasso(max_iter=100000))
    ]),
    param_grid=griglia_log,
    cv=5,
    scoring="neg_mean_squared_error"
)

ricerca_log.fit(X_train, y_train_log)

print("Miglior alpha:", ricerca_log.best_params_)

miglior_modello_log = ricerca_log.best_estimator_
y_pred_log = miglior_modello_log.predict(X_test)
y_pred_dollari = np.expm1(y_pred_log)
y_test_dollari = np.expm1(y_test_log)

print("MAE (dollari):", mean_absolute_error(y_test_dollari, y_pred_dollari))
print("RMSE (dollari):", mean_squared_error(y_test_dollari, y_pred_dollari) ** 0.5)
print("R2:", r2_score(y_test_dollari, y_pred_dollari))



"""
RMSE è sceso parecchio (da 33547 a 28472): coerente con la teoria —
 l'RMSE penalizza di più gli errori grandi, ed è proprio sulle case costose
 (quelle che creavano la skewness) che il log ha aiutato di più a "raddrizzare" 
 il comportamento del modello lineare
"""


"""
STEP 9 - Proviamo ad aggiungere delle features interessanti a partire da quelle date nel dataset

"""
def aggiungi_features(df):
    
    df = df.copy()

    # Superficie totale della casa
    df["TotalSF"] = (
        df["TotalBsmtSF"].fillna(0) +
        df["1stFlrSF"].fillna(0) +
        df["2ndFlrSF"].fillna(0)
    )

    # Numero totale equivalente di bagni
    # mezzo bagno viene contato come 0.5
    df["TotalBathrooms"] = (
        df["FullBath"].fillna(0) +
        0.5 * df["HalfBath"].fillna(0) +
        df["BsmtFullBath"].fillna(0) +
        0.5 * df["BsmtHalfBath"].fillna(0)
    )

    # Età della casa al momento della vendita
    df["HouseAge"] = df["YrSold"] - df["YearBuilt"]

    # Anni trascorsi dall'ultima ristrutturazione alla vendita
    df["RemodAge"] = df["YrSold"] - df["YearRemodAdd"]

    # Superficie totale dei portici
    df["TotalPorchSF"] = (
        df["OpenPorchSF"].fillna(0) +
        df["EnclosedPorch"].fillna(0) +
        df["3SsnPorch"].fillna(0) +
        df["ScreenPorch"].fillna(0)
    )

    # Feature binarie: presenza o assenza di alcune caratteristiche
    df["HasGarage"] = (df["GarageArea"].fillna(0) > 0).astype(int)
    df["HasBsmt"] = (df["TotalBsmtSF"].fillna(0) > 0).astype(int)
    df["HasFireplace"] = (df["Fireplaces"].fillna(0) > 0).astype(int)
    df["HasPool"] = (df["PoolArea"].fillna(0) > 0).astype(int)

    return df

df = aggiungi_features(df)
df_encoded = pd.get_dummies(df, columns=colonne_categoriche,drop_first=True)


X = df_encoded.drop(columns=["SalePrice", "Id"])  
y = df_encoded["SalePrice"]
y_log = np.log1p(y) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_train_log = np.log1p(y_train)
y_test_log = np.log1p(y_test)

ricerca_log.fit(X_train, y_train_log)

print("\n with additional features")
print("Miglior alpha:", ricerca_log.best_params_)

miglior_modello_log = ricerca_log.best_estimator_
y_pred_log = miglior_modello_log.predict(X_test)
y_pred_dollari = np.expm1(y_pred_log)
y_test_dollari = np.expm1(y_test_log)

print("MAE (dollari):", mean_absolute_error(y_test_dollari, y_pred_dollari))
print("RMSE (dollari):", mean_squared_error(y_test_dollari, y_pred_dollari) ** 0.5)
print("R2:", r2_score(y_test_dollari, y_pred_dollari))

"""
STEP 10 - Random Forest
========================
A differenza dei modelli lineari, Random Forest non richiede scaling
delle feature (gli alberi dividono per soglie, non per distanze).
Usiamo GridSearchCV per cercare i migliori iperparametri.
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Ricreiamo train/test in modo esplicito e pulito (niente variabili "fantasma")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_train_log = np.log1p(y_train)
y_test_log = np.log1p(y_test)

# Random Forest NON va dentro una Pipeline con scaler: non serve, lo scaler
# sarebbe solo overhead inutile (ma non farebbe danni se lo lasciassi).
modello_rf = RandomForestRegressor(random_state=42)

# Griglia di iperparametri principali:
# - n_estimators: numero di alberi nella foresta (più alberi = più stabile, ma più lento)
# - max_depth: profondità massima di ogni albero (None = nessun limite, rischio overfitting)
# - min_samples_leaf: numero minimo di campioni per foglia (valori più alti = alberi più "generici", meno overfitting)
griglia_rf = {
    "n_estimators": [100, 300],
    "max_depth": [None, 10, 20],
    "min_samples_leaf": [1, 2, 5]
}

ricerca_rf = GridSearchCV(
    modello_rf,
    param_grid=griglia_rf,
    cv=5,
    scoring="neg_mean_squared_error",
    n_jobs=-1  # usa tutti i core disponibili della CPU, velocizza la ricerca
)

ricerca_rf.fit(X_train, y_train_log)

print("Migliori parametri RF:", ricerca_rf.best_params_)

miglior_rf = ricerca_rf.best_estimator_
y_pred_rf_log = miglior_rf.predict(X_test)
y_pred_rf_dollari = np.expm1(y_pred_rf_log)
y_test_dollari = np.expm1(y_test_log)

print("\n--- Random Forest ---")
print("MAE (dollari):", mean_absolute_error(y_test_dollari, y_pred_rf_dollari))
print("RMSE (dollari):", mean_squared_error(y_test_dollari, y_pred_rf_dollari) ** 0.5)
print("R2:", r2_score(y_test_dollari, y_pred_rf_dollari))

# Bonus interessante: feature importance, quali variabili contano di più per il modello
importanze = pd.Series(miglior_rf.feature_importances_, index=X_train.columns)
print("\nTop 10 feature più importanti:")
print(importanze.sort_values(ascending=False).head(10))




