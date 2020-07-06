def get_middle(s):
    long = len(s)
    if long % 2 == 0:
        mid = round(long / 2)
        mid2 = mid - 1
        liste = list(s)
        return liste[mid2] + liste[mid]
    else:
        mid = round((long - 1) / 2)
        liste = list(s)
        return liste[mid]