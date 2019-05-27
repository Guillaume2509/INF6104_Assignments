import re

# Le texte qui sera analysé
texte = "Dogs are nice animals. Cats are not. " \
      "My cat ate a mice. My dog once ate a fry. " \
      "My dog once ate a fry. My cat ate a mice. " \
      "The catalog of the best dogs is around here somewhere."

# Les deux Regex pour trouver tous les mots souhaité
resultat1 = re.findall("\\bdogs?\\b.*?\\bcats?\\b|\\bcats?\\b.*?\\bdogs?\\b ", texte, flags=re.IGNORECASE)
resultat2 = re.findall("(?!dogs|cats)(\\w{4,})", str(resultat1), flags=re.IGNORECASE)

# Les mots finaux imprimés
print(resultat2)