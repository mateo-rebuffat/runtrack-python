def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne : afficher '-'
            print('-' * width)
        else:
            # Lignes intérieures : afficher '|', espaces, et '|'
            print('|' + ' ' * (width - 2) + '|')

# Exemple d'utilisation avec width=10 et height=3
draw_rectangle(15, 5)
