for i in range (11):
    for j in range(1,11):
        M = j * i
        print( j, "x", i, "=", M)

somme = 0
ran = 20
for i in range(ran+1):
    somme = somme + i 

print("La somme des", ran, "premiers entiers positifs est de", somme)

C = 6
L = 4
for i in range(L):
    for j in range(C):
        print("*", end=" ")
    print()

def signe (A,B):
    if A * B > 0 :
        print("Les valeurs de A et B ont le même signe.")
    else:
        print("Les valeurs de A et B ont deux signes différents.")

def maximum(A,B):
    if A > B : 
        return A
    else :
        return B

def minimum (A,B):
    if A < B :
        return A
    else :
        return B

A = -3
B = 6
signe(A,B)
print("Le maximum est", maximum(A,B))
print("Le minimum est", minimum(A,B))

print("-----------------")

def get_vowels_numbers(word):
    # créer un compteur de voyelles
    nb_vowels = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # on ajoute un au compteur
            nb_vowels += 1

    # à la fin de la fonction, vous allez renvoyer le compteur
    return nb_vowels


word = input("Entrer un mot")
vowels_count = get_vowels_numbers(word)
print("Il y a", vowels_count, "voyelles dans le mot", word)

