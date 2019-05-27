import re
import glob
import ntpath


# Importation des fichiers du répertoire etext00
path = 'C:/Users/Guillaume/Desktop/INF6104/LivresGroupés/etext00/*.txt'
fichiers = glob.glob(path)


# Définition d'une fonction permettant de conserver le nom du fichier (et non de tout le "path") pour fin d'esthetique à l'impression
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# Regex sur chacun des livres du répertoire en plus d'imprimer et compter les fichiers possédant un "match"
sommefichiers = 0
for fichier in fichiers:
    with open(fichier, 'r') as f:
        pass

        nom = path_leaf(fichier)

        livre = f.read()

        resultat = re.search("\\bdogs?\\b.*?\\bcats?\\b|\\bcats?\\b.*?\\bdogs?\\b", livre, flags=re.IGNORECASE)

        if resultat:
            print("Le fichier «" + nom + "» contient une ligne ayant à la fois les mots «dog» et «cat»")
            sommefichiers = sommefichiers + 1

        f.close()


# Imprimer le nombre total de fichiers possédant un "match"
print("Au total, " + str(sommefichiers) + " fichiers contiennent une ligne ayant à la fois les mots «dog» et «cat»")