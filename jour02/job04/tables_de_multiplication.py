# Programme Python pour afficher les tables de multiplication de 1 à N

# Fonction pour afficher la table de multiplication pour un nombre donné
def afficher_table(nombre, limite):
    print(f"Table de multiplication pour {nombre} :")
    for i in range(1, limite + 1):
        resultat = nombre * i
        print(f"{nombre} * {i} = {resultat}")

# Saisie de l'entier N avec vérification
while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un entier valide.")

# Affichage des tables de multiplication de 1 à N
for j in range(1, N + 1):
    afficher_table(j, 10)  # Vous pouvez ajuster la limite (ici 10) selon vos besoins
    print("-" * 20)  # Ligne de séparation entre les tables
