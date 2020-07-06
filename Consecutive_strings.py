def longest_consec(strarr, k):
    if len(strarr) < k or k <= 0 or len(strarr) == 0:
        return ""

    phraseFinal = ""
    for i in range(len(strarr) - (k - 1)):
        test = strarr[i]
        for o in range(1, k):
            test = test + strarr[i+o]
        if len(test) > len(phraseFinal):
            phraseFinal = test
    return phraseFinal

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))