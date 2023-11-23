# signe.py

def affiche_signe(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("Le nombre est nul")

# Appel de la fonction avec différents paramètres
affiche_signe(5)
affiche_signe(-3)
affiche_signe(0)
