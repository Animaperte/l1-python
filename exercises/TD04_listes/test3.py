# Exercice 1 : faire un programme qui crée une liste de taille n pour n quelconque où chaque élément de la liste est un entier aléatoire
# compris entre 0 et 10

import random

n = int(input("Entrez un nombre n quelconque qui déterminera la taille de la liste"))
liste = []
while n > 0:
    liste.append(random.randint(0,10))
    n = n-1
print(liste)

# Exercice 2 :
L = 4
C = 
Listez = [random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4)]
def affiche_sudoku(y):
    for i in range(L):
        for j in range(C):
            print(Listez, end=" ")
        print()


affiche_sudoku(4)