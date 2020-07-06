def remove_char(s):
    L = list(s)
    L.pop(0)
    L.pop(-1)
    L = "".join(L)
    return L