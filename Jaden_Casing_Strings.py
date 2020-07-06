def to_jaden_case(string):
    liste = string.split()
    nbListe = len(liste)
    for index in range(0, nbListe):
        liste[index] = liste[index].capitalize()
    liste = " ".join(liste)
    return liste