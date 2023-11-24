def distance_parcourue(marches, hauteur_marche):
    hauteur_totale = marches * hauteur_marche * 2  # Le gardien monte et descend
    distance_m = hauteur_totale / 100  # Convertir en mètres
    distance_semaine = distance_m * 5  # Aller-retour aux toilettes cinq fois par jour
    distance_semaine *= 7  # Pour la semaine entière
    
    return distance_semaine

# Exemple d'utilisation
nombre_marches = 10
hauteur_marche_cm = 20

distance_semaine = distance_parcourue(nombre_marches, hauteur_marche_cm)

# Afficher le résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_semaine:.2f} m par semaine.")
