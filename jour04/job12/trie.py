def tri_croissant(liste):
    # Algorithme de tri par sélection
    n = len(liste)

    for i in range(n - 1):
        indice_min = i

        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        # Échanger les éléments
        temp = liste[i]
        liste[i] = liste[indice_min]
        liste[indice_min] = temp

# Exemple d'utilisation
L = [7, 11, 42, 39, 2]

print("Liste originale :", L)

# Appel de la fonction de tri
tri_croissant(L)

print("Liste triée dans l'ordre croissant :", L)
