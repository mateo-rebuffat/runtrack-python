# calculator.py

def calcule(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else:
        return "Opérateur non valide"

    return result

# Appel de la fonction avec différents paramètres
result1 = calcule(5, '+', 3)
result2 = calcule(10, '*', 2)
result3 = calcule(8, '/', 4)

# Affichage des résultats
print(result1)
print(result2)
print(result3)
