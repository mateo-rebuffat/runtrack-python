# Liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Filtrer les valeurs comprises dans l'intervalle [25, 90]
valeurs_intervalle = [valeur for valeur in L if 25 <= valeur <= 90]

# Calculer le produit des valeurs de l'intervalle
produit_valeurs_intervalle = 1
for valeur in valeurs_intervalle:
    produit_valeurs_intervalle *= valeur

# Afficher le résultat
print("Produit des valeurs dans l'intervalle [25, 90] :", produit_valeurs_intervalle)
