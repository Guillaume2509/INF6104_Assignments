from whoosh.qparser import QueryParser
from whoosh.index import open_dir

# Étape 1: ouverture de l'index
ix = open_dir("indexdir")

# Étape 2: création de la liste de mots
ListeMots = ["Cat", "Dog", "Elephant", "Kangaroo", "Lion", "Giraffe", "Gazelle", "Zebra", "Shark", "Whale",
        "Carriage", "Lorrie", "Train", "Airplane", "Steamship", "Submarine", "Balloon", "Space", "Raft", "Speedboat",
        "Amazingly", "Lovely", "Frankly", "Rapidly", "Slowly", "Kindly", "Angrily", "Surprisingly", "Demure", "Despot",
        "Feral", "Flabbergasted", "Forsake", "Landlord", "Haughty", "Innate", "Knell", "Lithe", "Modicum", "Nadir",
        "Perusal", "Quaint", "Staid", "Gerrymandering", "Zenith", "Playwright", "Oxyphenbutazone", "Muzjiks", "Xu", "Cwm"]

# Étape 3: itération, pour chaque mot de la recherche
# Étape 3.1: assignation de la fonction recherche
with ix.searcher() as searcher:

# Étape 3.2: itération de la recherche pour chaque paire
        for mot in ListeMots:

                qp = QueryParser("content", schema=ix.schema)
                q = qp.parse(str(mot))

                with ix.searcher() as s:
                        results = s.search(q, limit=None)


                # Étape 5.3: affichage du résultat
                print("Mot: " + mot + "\nNombre de documents: " + str(len(results)) + "\n")
