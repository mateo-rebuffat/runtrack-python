def chiffrement_cesar(message, decalage):
    resultat = ""

    for caractere in message:
        if caractere.isalpha():  # Vérifier si le caractère est une lettre
            decalage_absolu = abs(decalage)
            if caractere.islower():
                resultat += chr((ord(caractere) - ord('a') + decalage_absolu) % 26 + ord('a')) if decalage > 0 else chr((ord(caractere) - ord('a') - decalage_absolu) % 26 + ord('a'))
            elif caractere.isupper():
                resultat += chr((ord(caractere) - ord('A') + decalage_absolu) % 26 + ord('A')) if decalage > 0 else chr((ord(caractere) - ord('A') - decalage_absolu) % 26 + ord('A'))
        else:
            resultat += caractere

    return resultat

# Exemple d'utilisation
message_original = "Bonjour, Jules César!"
decalage_cesar = 3
message_chiffre = chiffrement_cesar(message_original, decalage_cesar)

print("Message original:", message_original)
print("Message chiffré:", message_chiffre)
