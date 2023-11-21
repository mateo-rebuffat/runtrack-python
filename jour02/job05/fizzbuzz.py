# Programme Python pour FizzBuzz

# Itérer les nombres de 1 à 100 inclus
for nombre in range(1, 101):
    # Vérifier si le nombre est un multiple de trois et/ou de cinq
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre % 3 == 0:
        print("Fizz")
    elif nombre % 5 == 0:
        print("Buzz")
    else:
        print(nombre)
