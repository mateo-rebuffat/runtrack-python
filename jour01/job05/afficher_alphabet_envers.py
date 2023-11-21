# Programme Python pour afficher l'alphabet à l'envers

# Boucle pour itérer à travers les caractères ASCII de 'z' à 'a' dans l'ordre décroissant
for lettre in range(ord('z'), ord('a') - 1, -1):
    print(chr(lettre), end=' ')

# Saut de ligne à la fin
print()
