def draw_triangle(height):
    for i in range(height):
        # Espaces à gauche
        espaces_gauche = ' ' * (height - i - 1)
        
        # Caractères pour former le triangle
        if i == 0:
            # Première ligne : '_'
            ligne = '_'
        elif i == height - 1:
            # Dernière ligne : '-' * largeur
            ligne = '-' * (2 * i + 1)
        else:
            # Lignes intermédiaires : '/', espaces, '\'
            ligne = '/' + ' ' * (2 * i - 1) + '\\'
        
        # Afficher la ligne
        print(espaces_gauche + ligne)

# Demander à l'utilisateur de saisir la hauteur du triangle
hauteur = int(input("Veuillez entrer la hauteur du triangle : "))

# Appel de la fonction pour dessiner le triangle
draw_triangle(hauteur)
