from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import time

# Étape 1: création de la fonction de combinaison et ouverture de l'index
def tessa(source):
        result = []
        for p1 in range(len(source)):
                for p2 in range(p1+1,len(source)):
                        result.append([source[p1],source[p2]])
        return result

ix = open_dir("indexdir")

# Étape 2: création de la liste de mots
ListeMots = ["Cat", "Dog", "Elephant", "Kangaroo", "Lion", "Giraffe", "Gazelle", "Zebra", "Shark", "Whale",
        "Carriage", "Lorrie", "Train", "Airplane", "Steamship", "Submarine", "Balloon", "Space", "Raft", "Speedboat",
        "Amazingly", "Lovely", "Frankly", "Rapidly", "Slowly", "Kindly", "Angrily", "Surprisingly", "Demure", "Despot",
        "Feral", "Flabbergasted", "Forsake", "Landlord", "Haughty", "Innate", "Knell", "Lithe", "Modicum", "Nadir",
        "Perusal", "Quaint", "Staid", "Gerrymandering", "Zenith", "Playwright", "Oxyphenbutazone", "Muzjiks", "Xu", "Cwm"]

# Étape 4: combinaison des paires à l'aide de la fonction de combinaison.
pairings = tessa(ListeMots)
print("%d pairings" % len(pairings) + "\n")

# Étape 5: itération, pour chaque mot, de la recherche et du temps de requête moyen
# Étape 5.1: assignation de la fonction recherche
with ix.searcher() as searcher:

# Étape 5.2: itération de la recherche pour chaque paire
        for pair in pairings:

                debut = time.time()

                qp = QueryParser("content", schema=ix.schema)
                q = qp.parse(str(pair))  #À noter, en présence de plusieurs strings, le lien AND est appliqué par défaut

                i = 1
                while i <= 10:
                        with ix.searcher() as s:
                                results = s.search(q, limit=None)

                        i = i + 1

                fin = time.time()
                TempsRecherche = (fin - debut)/10

                # Étape 5.3: affichage du résultat
                print("Paire: " + str(pair) + "\nNombre de documents: " + str(len(results)) + "\nTemps de requête moyen (en secondes): " + str(TempsRecherche) + "\n")

