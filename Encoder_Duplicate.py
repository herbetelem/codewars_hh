def duplicate_encode(word):
    result = ""
    word = word.lower()
    for index in range(len(word)):
        if word.count(word[index]) > 1:
            result = result + ")"
        else:
            result = result + "("
    return result