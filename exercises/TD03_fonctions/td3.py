# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en s de tps donné comme j, h, m, s."""
    return(temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3])


temps = (3, 23, 1, 34)
print(type(temps))
ma_valeur = tempsEnSeconde(temps)
print(ma_valeur)


def secondeEnTemps(seconde):
    """Renvoie le tps (j, h, m, s) qui correspond au nb de s passé en arg"""
    jours = seconde // 86400
    heures = (seconde - jours*86400) // 3600
    minutes = (seconde - jours*86400 - heures*3600) // 60
    secondes = (seconde - jours*86400 - heures*3600 - minutes*60)
    return(jours, heures, minutes, secondes)


tempsz = secondeEnTemps(100000)
print(tempsz[0], "j", tempsz[1], "h", tempsz[2], "m", tempsz[3], "s")

# fonction auxiliaire qui permet d'afficher le temps


def afficheTemps(temps):
    j, h, m, s = temps
    if j != 0 and j > 1:
        jours = str(j)+" jour"+"s"
    elif j == 0:
        jours = ""
    else:
        jours = str(j)+" jour"
    if h != 0 and h > 1:
        heures = str(h)+" heure"+"s"
    elif h == 0:
        heures = ""
    else:
        heures = str(h)+" heure"
    if m != 0 and m > 1:
        minutes = str(m)+" minute"+"s"
    elif m == 0:
        minutes = ""
    else:
        minutes = str(m)+" minute"
    if s != 0 and s > 1:
        secondes = str(s)+" seconde"+"s"
    elif s == 0:
        secondes = ""
    else:
        secondes = str(s)+" seconde"
    print(jours, heures, minutes, secondes)


temps = 1, 0, 14, 23
afficheTemps(temps)


def demandeTemps(tempsw):
    j = int(input("rentrez le nombre de jours "))
    h = int(input("rentrez le nombre d'heures "))
    while h > 23:
        h = int(input("rentrez le nombre d'heures "))
    m = int(input("rentrez le nombre de minutes "))
    if m > 59:
        m = int(input("rentrez le nombre de minutes "))
    s = int(input("rentrez le nombre de secondes "))
    if s > 59:
        s = int(input("rentrez le nombre de secondes "))
    tempsw = (j, h, m, s)
    return tempsw


tempsw = demandeTemps
afficheTemps(demandeTemps(tempsw))


def sommeTemps(temps1, temps2):
    j1, h1, m1, s1 = temps1
    j2, h2, m2, s2 = temps2
    j3 = j1 + j2
    h3 = h1 + h2
    while h3 > 23:
        j3 = j3 + 1
        h3 = h3 - 24
    m3 = m1 + m2
    while m3 > 59:
        h3 = h3 + 1
        m3 = m3 - 60
    s3 = s1 + s2
    while s3 > 59:
        m3 = m3 + 1
        s3 = s3 - 60
    temps3 = (j3, h3, m3, s3)
    return afficheTemps(temps3)


sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))


def proportionTemps(temps, proportion):
    temps = tempsEnSeconde(temps)
    newtemps = proportion * temps
    newtemps = secondeEnTemps(newtemps)
    return newtemps


afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))


def tempsEnDate(temps):
    pass


def afficheDate(date=-1):
    pass


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()
