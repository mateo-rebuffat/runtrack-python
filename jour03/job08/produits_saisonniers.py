# produits_saisonniers.py

def affiche_produits_saisonniers(type_produit, saison):
    if type_produit == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type_produit == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type_produit == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type_produit == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucun produit correspondant trouvé.")

# Appel de la fonction avec différents paramètres
affiche_produits_saisonniers("fruits", "hiver")
affiche_produits_saisonniers("fruits", "ete")
affiche_produits_saisonniers("legume", "hiver")
affiche_produits_saisonniers("legume", "ete")

