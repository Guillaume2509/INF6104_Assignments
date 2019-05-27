#Guillaume Giroux, 16133519, Travail Noté 5, Question 2
import numpy as np
from sklearn.preprocessing import normalize

#Entrée
Lien1 = "index.html"
LienDepart = "velo.html"
Lien3 = "menu.html"
ListeLiens = [Lien1, LienDepart, Lien3]

MatriceA = np.array([[0, 0, 0],
                     [1, 0, 1],
                     [1, 1, 0]])

i = 1
Hub = np.array([[1],[1],[1]])
while i <= 10:
    Authority = np.matmul(MatriceA,Hub)
    Hub = np.matmul(MatriceA.transpose(),Authority)
    Authority = normalize(Authority, axis=0, norm='l2')
    Hub = normalize(Hub, axis=0, norm='l2')
    i = i + 1

#Arondir à deux décimales les valeurs et ajuster pour bien imprimer sans crochet
Authority = np.round(Authority, decimals=2)
Hub = np.round(Hub, decimals=2)
Authority = np.hstack(Authority)
Hub = np.hstack(Hub)

#Imprimer les coefficient Authority et Hub pour chaque lien - Sortie finale
for lien, a, h in zip(ListeLiens, Authority, Hub):
    print("Pour " + lien + ", le coefficient Authority est de " + str(a) + " et le coefficient Hub est de " + str(h))

#Imprimer les pages recommandées de l'algorithme HITS - Sortie finale
print("\n")
for lien, a, h in zip(ListeLiens, Authority, Hub):
    if a > 0.01:
        print("L'algorithme HITS recommande la page " + lien)
    elif a <= 0.01:
        print("L'algorithme HITS ne recommande pas la page " + lien)

print("\nNous pouvons voir que l'algorithme HITS indique ici que les pages velo.html et menu.html sont des autorités \nalors que la page index.html est vue comme étant un Hub et ne la recommande pas du tout.")