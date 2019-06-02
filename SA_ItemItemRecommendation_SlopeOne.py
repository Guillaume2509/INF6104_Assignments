import numpy as np
import pandas as pd
from surprise import SlopeOne
from surprise import Dataset
from surprise import accuracy
from surprise import Reader
from surprise.model_selection import train_test_split

# Arrangement des données en un jeu P et un jeu de test
NaN = np.nan
data = {"Jean": [7, NaN, 8, 7],
        "Marie": [6, 5, NaN, 2],
        "Pierre": [NaN, 2, 2, 5],
        "Luc": [1, 3, 4, 1],
        "Guy": [2, NaN, 2, 1]}
data = pd.DataFrame.from_dict(data, orient='index', columns=['Article 1', 'Article 2', 'Article 3', 'Article 4'])
tidydata = pd.melt(
    data.reset_index(),
    id_vars = 'index',
    value_vars = data.columns,
)
tidydata.columns = ['Utilisateur', "Article", "Score"]
tidydata = tidydata.dropna()
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(tidydata[['Utilisateur', "Article", "Score"]], reader)
trainset, testset = train_test_split(data, test_size=0.40, random_state=42)

# Création de l'algorithme du filtrage collaboratif utilisateur-utilisateur utilisant SlopeOne
algo = SlopeOne()
algo.fit(trainset)

# Application de l'algorithme sur le jeu du test
test_pred = algo.test(testset)

# Calculer la All-But-1 MAE
AllBut1 = accuracy.mae(test_pred, verbose=False)
AllBut1 = round(AllBut1, 2)

print("L’erreur de validation croisée (All-But-1 MAE) en utilisant l’algorithme Slope One est de " + str(AllBut1))