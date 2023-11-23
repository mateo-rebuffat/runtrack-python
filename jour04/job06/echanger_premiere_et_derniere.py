def echanger_premiere_et_derniere(liste):
    if len(liste) > 1:
        premiere_valeur = liste[0]
        derniere_valeur = liste[-1]
        liste[0] = derniere_valeur
        liste[-1] = premiere_valeur

# Liste originale
liste = [1, 2, 3, 4, 5]
print(liste)

# Échanger les valeurs de la première et de la dernière case
echanger_premiere_et_derniere(liste)
print(liste)
