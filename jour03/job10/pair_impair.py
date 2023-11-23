# pair_impair.py

def verifie_pair_impair(nombre):
    # Vérifier si le nombre est un chiffre entier et positif
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif ou entier.")

# Appel de la fonction avec différentes valeurs
verifie_pair_impair(10)
verifie_pair_impair(7)
verifie_pair_impair(13)
verifie_pair_impair(-5)  # Test avec un nombre négatif
verifie_pair_impair(3.5)  # Test avec un nombre décimal
verifie_pair_impair("abc")  # Test avec une chaîne de caractères
