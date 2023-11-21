# Programme Python pour afficher les nombres de 0 à 100 (exclusion de 26, 37, 88)

# Boucle pour parcourir les nombres de 0 à 100 inclus
for nombre in range(101):
    if nombre not in [26, 37, 88]:
        print(nombre)
