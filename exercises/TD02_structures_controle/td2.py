# Exercice 1
print(len("AbC"*6))

# Exercice 2
x = int(input("Veuillez choisir un nombre entier : "))
if x % 2 == 0:
    print("le nombre est pair")
else:
    print("le nombre est impair")

# Exercice 3
n = int(input("Veuilez saisir un nombre entier : "))
for i in range(1, n+1):
    N = n % i
    if N == 0:
        print(i)
    else:
        continue
