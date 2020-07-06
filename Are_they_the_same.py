def comp(array1, array2):
    if isinstance(array1, list) and isinstance(array2, list) and len(array1) == len(array2):
        array1.sort(key=abs)
        array2.sort(key=abs)
        result = True
        for i in range(len(array1)):
            if array1[i] * array1[i] != array2[i]:
                result = False
    else:
        result = False
    return result


a1 = [1, 3, 7, 21, 85, 87, 70]
a2 = [1, 9, 49, 441, 4900, 7225, 7569]
print(comp(a1, a2))
