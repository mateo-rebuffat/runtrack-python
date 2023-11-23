def arrondir_et_trier(liste):
    # Fonction pour arrondir chaque nombre dans la liste
    def arrondir_nombre(nombre):
        partie_entiere = int(nombre)
        partie_fractionnaire = nombre - partie_entiere

        # Arrondir la partie fractionnaire à 1 décimale
        if partie_fractionnaire >= 0.5:
            return partie_entiere + 1
        else:
            return partie_entiere

    # Appliquer la fonction d'arrondi à chaque élément de la liste
    liste_arrondie = [arrondir_nombre(nombre) for nombre in liste]

    # Algorithme de tri par sélection pour trier la liste
    n = len(liste_arrondie)

    for i in range(n - 1):
        indice_min = i

        for j in range(i + 1, n):
            if liste_arrondie[j] < liste_arrondie[indice_min]:
                indice_min = j

        # Échanger les éléments
        temp = liste_arrondie[i]
        liste_arrondie[i] = liste_arrondie[indice_min]
        liste_arrondie[indice_min] = temp

    return liste_arrondie

# Exemple d'utilisation
liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appel de la fonction pour arrondir et trier
liste_arrondie_et_triee = arrondir_et_trier(liste)

# Afficher le résultat
print("Liste arrondie et triée :", liste_arrondie_et_triee)
