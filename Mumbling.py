def accum(s):
    liste = list(s)
    nbListe = len(liste) + 1
    result = ""
    compteur = 1
    while compteur < nbListe:
        index = compteur - 1
        liste[index] = liste[index] * compteur
        liste[index] = liste[index].capitalize()
        result = result + liste[index]
        compteur = compteur + 1
        if compteur < nbListe:
            result = result + "-"
    return result