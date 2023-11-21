def type_triangle(a, b, c):
    # Vérifier si les longueurs permettent de construire un triangle
    if a + b > c and a + c > b and b + c > a:
        # Triangle quelconque
        if a != b and b != c and a != c:
            return "Triangle quelconque"
        # Triangle équilatéral
        elif a == b and b == c:
            return "Triangle équilatéral"
        # Triangle isocèle
        elif a == b or b == c or a == c:
            # Vérifier si le triangle est rectangle
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
                return "Triangle isocèle et rectangle"
            else:
                return "Triangle isocèle"
        else:
            return "Erreur indéterminée"
    else:
        return "Impossible de construire un triangle"

# Saisie des longueurs a, b, c
while True:
    try:
        a = float(input("Entrez la longueur a : "))
        b = float(input("Entrez la longueur b : "))
        c = float(input("Entrez la longueur c : "))
        break
    except ValueError:
        print("Veuillez entrer des nombres valides.")

# Déterminer et afficher le type de triangle
resultat = type_triangle(a, b, c)
print(resultat)
