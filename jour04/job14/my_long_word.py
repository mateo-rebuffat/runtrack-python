def est_espace(caractere):
    # Vérifie si le caractère est un espace
    return caractere == ' '

def my_long_word(longueur_min, phrase):
    mots = []  # Liste pour stocker les mots plus longs que la longueur minimale
    mot_en_cours = ''  # Variable pour stocker le mot en cours de construction

    # Itérer à travers chaque caractère dans la phrase
    for caractere in phrase:
        if not est_espace(caractere):
            # Si le caractère n'est pas un espace, ajouter à mot_en_cours
            mot_en_cours += caractere
        elif mot_en_cours:
            # Si on rencontre un espace et mot_en_cours n'est pas vide, vérifier sa longueur
            if len(mot_en_cours) > longueur_min:
                mots.append(mot_en_cours)
            mot_en_cours = ''  # Réinitialiser le mot_en_cours

    # Vérifier le dernier mot après la fin de la phrase
    if mot_en_cours and len(mot_en_cours) > longueur_min:
        mots.append(mot_en_cours)

    # Concaténer les mots en une chaîne de caractères
    resultat = ' '.join(mots)

    return resultat

# Exemple d'utilisation
longueur_min = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

# Appel de la fonction
resultat = my_long_word(longueur_min, phrase)

# Afficher le résultat
print("Output :", resultat)
