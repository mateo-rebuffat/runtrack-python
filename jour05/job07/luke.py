def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            # Si l'étudiant a échoué, la note reste inchangée
            notes_arrondies.append(note)
        else:
            # Calculer le prochain multiple de 5 supérieur ou égal à la note
            prochain_multiple_de_5 = (note // 5 + 1) * 5

            # Vérifier si la note doit être arrondie
            if prochain_multiple_de_5 - note < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
notes_eleves = [78, 42, 91, 65, 39, 88]
notes_arrondies = arrondir_notes(notes_eleves)

# Afficher le résultat
print("Notes d'origine :", notes_eleves)
print("Notes arrondies :", notes_arrondies)
