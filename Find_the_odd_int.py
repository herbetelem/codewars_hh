def find_it(seq):
    compteur = 0
    final = 0
    seq.sort()
    while compteur < len(seq):
        count = 0
        index = compteur
        while index < len(seq) and seq[compteur] == seq[index]:
            count +=1
            index +=1
        if count % 2 > 0:
            final = seq[compteur]
        compteur = compteur + count
    return final