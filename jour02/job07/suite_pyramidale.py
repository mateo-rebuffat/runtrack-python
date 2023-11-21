# Programme Python pour créer une suite pyramidale

# Chaîne de caractères initiale
chaine_initiale = "abcdefghijklmnopqrstuvwxyz" * 10

# Nombre de caractères par ligne
caracteres_par_ligne = 1

# Afficher la suite pyramidale
for i in range(len(chaine_initiale)):
    print(chaine_initiale[i] * caracteres_par_ligne)
    caracteres_par_ligne += 1
