# Ecrire dans un fichier
aw = (15+5+13)/3
az = (10 + 8 + 19)/3
ay = (3+9+7)/3
av = (15+17+11)/3
al = (9 + 10 + 12)/3
Monfichier = open("notes.txt", "w")
Monfichier.write(str(aw) + '\n')
Monfichier.write(str(az) + '\n')
Monfichier.write(str(ay) + '\n')
Monfichier.write(str(av) + '\n')
Monfichier.write(str(al))

Monfichier.close()