def remplacer_par_somme_voisins(liste):
    if len(liste) >= 5:
        somme_voisins = liste[2] + liste[4]
        liste[3] = somme_voisins

# Créer une liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Afficher la première liste des 5 entiers
print(L)

# Afficher la deuxième valeur de la liste
deuxieme_valeur = L[1]
print(deuxieme_valeur)

# Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4], puis afficher à nouveau le tableau.
remplacer_par_somme_voisins(L)
print(L)

# Afficher la dernière valeur de la liste
derniere_valeur = L[-1]
print(derniere_valeur)
