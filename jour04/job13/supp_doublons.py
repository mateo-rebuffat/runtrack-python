def supprimer_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

# Exemple d'utilisation
liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

print("Liste originale :", liste)

# Appel de la fonction pour supprimer les doublons
liste_sans_doublons = supprimer_doublons(liste)

print("Liste sans doublons :", liste_sans_doublons)
