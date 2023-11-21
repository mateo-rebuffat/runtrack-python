# Variables représentant un produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_en_stock = 50

# Afficher les informations du produit
print("Informations du produit:")
print("Nom du produit:", nom_produit)
print("Prix unitaire:", prix_unitaire)
print("Quantité en stock:", quantite_en_stock)

# Ajouter des produits en stock
quantite_achetee = int(input("\nSaisissez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock += quantite_achetee

# Mise à jour du prix avec une augmentation de 10%
prix_unitaire *= 1.1

# Afficher à nouveau les informations sur le produit
print("\nInformations mises à jour du produit après l'achat et l'augmentation de prix:")
print("Nom du produit:", nom_produit)
print("Prix unitaire (avec augmentation de 10%):", prix_unitaire)
print("Quantité en stock après l'achat:", quantite_en_stock)
