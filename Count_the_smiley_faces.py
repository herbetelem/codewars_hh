def count_smileys(arr):
    count = 0
    for index in arr:
        if len(index) == 2:
            if (index[0] == ":" or index[0] == ";") and (index[1] == ")" or index[1] == "D"):
                count += 1
        elif len(index) == 3:
            if (index[0] == ":" or index[0] == ";") and (index[1] == "-" or index[1] == "~") and (index[2] == ")" or index[2] == "D"):
                count += 1
    return count