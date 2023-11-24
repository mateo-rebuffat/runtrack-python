def creer_tapis(n):
    print("+" + "-" * n + "+")
    for i in range(1, n):
        for j in range(n+1):
            if i == n - j:
                print(" ", end="")
            else:
                print("#", end="")
        print()
    print("+" + "-" * n + "+")

# Testons la fonction avec n = 10
creer_tapis(10)
