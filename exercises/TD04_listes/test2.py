print("listes")
print("")
from random import shuffle
 
# Générateur de phrases
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4"
chained_words = input("Entrer une chaine de la forme mot1/mot2/mot3/mot4")
 
# transformer cette chaine en liste
words = chained_words.split("/")
 
# la melanger
shuffle(words)
 
# recuperer le nombre d'elements
words_len = len(words)
 
# si le nombre d'élements de cette liste est inferieur à 10
if words_len < 10:
  # afficher les deux premiers mots
  print(words[0], words[1])
  
# si le nombre d'éements est superieur ou égal à 10
else:
  # afficher les 3 derniers
  print(words[words_len - 1], words[words_len - 2], words[words_len - 3])

print("")
print("fonctions")
print("")

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