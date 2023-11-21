# Initialisation des variables
montant_initial = 10000.0  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5.0  # Taux de rendement annuel en pourcentage

# Afficher le gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel initial :", gain_annuel)

# Augmentation du capital et du taux de rendement
montant_initial += 5000.0
taux_rendement_annuel += 2.0

# Calculer à nouveau le gain annuel après augmentation
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Nouveau gain annuel après augmentation :", nouveau_gain_annuel)

# Retrait d'une partie du montant et diminution du rendement
montant_initial -= 0.1 * montant_initial  # Retrait de 10%
taux_rendement_annuel -= 1.0

# Calculer le montant final de l'investissement après retrait
montant_final = montant_initial + nouveau_gain_annuel

# Afficher le nouveau gain après retrait
nouveau_gain_final = (taux_rendement_annuel / 100) * montant_final
print("Nouveau gain après retrait :", nouveau_gain_final)
