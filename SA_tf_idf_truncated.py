import pandas as pd
import numpy as np

### Question 1, termes tronqués
## Calcul du facteur idf pour chaque mot
# Création des listes et de la constante D
ListeTermes = ["Luc", "cra", "rou", "mai", "pol", "con", "sou"]
df = [1, 2, 4, 2, 1, 1, 1]
D = 4

# Création du dictionnaire
DictTermesEtDf = {'terme':ListeTermes, 'df':df}

# Conversion du dictionnaire en tableau
DataFrameTermesEtDf = pd.DataFrame(DictTermesEtDf)

# Calcul de la colonne
DataFrameTermesEtDf = DataFrameTermesEtDf.assign(idf = np.log2(D/DataFrameTermesEtDf.df))

# Imprimer le nouveau tableau
print(DataFrameTermesEtDf)

## Transformation de chaque document en vecteur tf.idf
D1sansidf = [1, 1, 1, 0, 0, 0, 0]
D2sansidf = [0, 0, 1, 1, 0, 0, 0]
D3sansidf = [0, 1, 2, 1, 0, 0, 0]
D4sansidf = [0, 0, 2, 0, 1, 1, 1]

idf = DataFrameTermesEtDf['idf']

D1avecidf = D1sansidf * idf
D2avecidf = D2sansidf * idf
D3avecidf = D3sansidf * idf
D4avecidf = D4sansidf * idf

Dictidfdocus = {'Terme':ListeTermes, 'Document 1':D1avecidf, 'Document 2':D2avecidf, 'Document 3':D3avecidf, 'Document 4':D4avecidf}

DataFrameidfdocus = pd.DataFrame(Dictidfdocus)

print(DataFrameidfdocus)

## Calcul de la similarité entre chaque document

from scipy import spatial

print(1 - spatial.distance.cosine(D1avecidf, D1avecidf))
print(1 - spatial.distance.cosine(D1avecidf, D2avecidf))
print(1 - spatial.distance.cosine(D1avecidf, D3avecidf))
print(1 - spatial.distance.cosine(D1avecidf, D4avecidf))
print(1 - spatial.distance.cosine(D2avecidf, D1avecidf))
print(1 - spatial.distance.cosine(D2avecidf, D2avecidf))
print(1 - spatial.distance.cosine(D2avecidf, D3avecidf))
print(1 - spatial.distance.cosine(D2avecidf, D4avecidf))
print(1 - spatial.distance.cosine(D3avecidf, D1avecidf))
print(1 - spatial.distance.cosine(D3avecidf, D2avecidf))
print(1 - spatial.distance.cosine(D3avecidf, D3avecidf))
print(1 - spatial.distance.cosine(D3avecidf, D4avecidf))
print(1 - spatial.distance.cosine(D4avecidf, D1avecidf))
print(1 - spatial.distance.cosine(D4avecidf, D2avecidf))
print(1 - spatial.distance.cosine(D4avecidf, D3avecidf))
print(1 - spatial.distance.cosine(D4avecidf, D4avecidf))

## Calcul du document étant le plus pertinent selon le modèle vectoriel tf.idf avec les termes de recheche "maison" et "rouge"
# "maison" et "rouge" nous donnerait le vecteur [0, 0, 1, 1, 0, 0, 0]

mairou = [0, 0, 1, 1, 0, 0, 0]

print("Le pourcentage de pertinence est de : " + str((1 - spatial.distance.cosine(mairou, D1avecidf))*100) + "%")
print("Le pourcentage de pertinence est de : " + str((1 - spatial.distance.cosine(mairou, D2avecidf))*100) + "%")
print("Le pourcentage de pertinence est de : " + str((1 - spatial.distance.cosine(mairou, D3avecidf))*100) + "%")
print("Le pourcentage de pertinence est de : " + str((1 - spatial.distance.cosine(mairou, D4avecidf))*100) + "%")

## Calcul du score de Hiemstra et al. simplifié
print(D1avecidf/D)