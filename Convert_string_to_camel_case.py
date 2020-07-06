def to_camel_case(text):
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    text = text.split(" ")
    for index in range(len(text)):
        if index > 0:
            text[index] = text[index].capitalize()
    text = "".join(text)
    return text