def my_sort(liste):
    # Initialiser le nombre total de coups
    total_coups = 0
    
    # Indicateur pour savoir si des échanges ont été effectués pendant la passe courante
    echanges_effectues = True
    
    # Tant qu'il y a des échanges à faire, continuez le tri
    while echanges_effectues:
        echanges_effectues = False  # Réinitialiser l'indicateur à chaque début de passe
        for i in range(len(liste) - 1):
            # Comparer les éléments adjacents et échanger s'ils sont dans le mauvais ordre
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echanges_effectues = True  # Indiquer qu'un échange a été effectué
                total_coups += 1  # Incrémenter le nombre total de coups
    
    # Afficher le nombre total de coups
    print("Nombre total de coups nécessaires pour trier la liste :", total_coups)
    
    return liste

# Exemple d'utilisation
liste_non_triee = [64, 34, 25, 12, 22, 11, 90]
liste_triee = my_sort(liste_non_triee.copy())

# Afficher le résultat
print("Liste triée :", liste_triee)
