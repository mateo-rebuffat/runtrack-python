# time_to_text.py

def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0:
            print(f"{minutes} minutes")
        elif heures == 1:
            print(f"{heures} heure et {minutes_restantes} minutes")
        else:
            print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appel de la fonction avec différentes valeurs
time_to_text(120)
time_to_text(75)
time_to_text(45)
time_to_text(104)
time_to_text(-30)  # Test avec un nombre négatif
time_to_text(90.5)  # Test avec un nombre décimal
time_to_text("abc")  # Test avec une chaîne de caractères
