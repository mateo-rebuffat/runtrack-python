# Liste
L = [8, 24, 48, 2, 16]

# Compter le nombre de multiples de 3
nombre_multiples_de_3 = sum(1 for nombre in L if nombre % 3 == 0)

# Afficher le résultat
print("Nombre de multiples de 3 dans la liste :", nombre_multiples_de_3)
