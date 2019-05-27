#Guillaume Giroux, 16133519, Travail Noté 5, Question 1
import numpy as np

#Entrée
Lien1 = "index.html"
Lien2 = "velo.html"
Lien3 = "page.html"
Lien4 = "menu.html"
ListeLiens = [Lien1, Lien2, Lien3, Lien4]

MatriceTransition = np.array([[0, 1/3, 1/3, 1/3],
                              [0, 0, 0, 1],
                              [1, 0, 0, 0],
                              [0, 1/2, 1/2, 0]])


#Générer le vecteur probabilité
ListeProbabilité = []
for x in range(len(ListeLiens)):
     ListeProbabilité.append(1/len(ListeLiens))

VecteurProbabilité = np.array(ListeProbabilité)


#Itération pour obtenir la matrice finale de la chaîne de Markov
MatriceItérée = np.linalg.matrix_power(MatriceTransition, 1000)


#Multiplication du vecteur de probabilité par la matrice itérée
VecteurPageRank = np.matmul(VecteurProbabilité, MatriceItérée)


#Imprimer le score PageRank pour chaque lien - Sortie finale
for lien, PageRank in zip(ListeLiens, VecteurPageRank):
    print("Le score PageRank de " + lien + " est de " + str(PageRank))

print("\nNous pouvons voir que la page menu.html est celle ayant le PageRank le plus élévé. \nCeci est dû au fait qu'elle reçois des liens de meilleure qualité.")