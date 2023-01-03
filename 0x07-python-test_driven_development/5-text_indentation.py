def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}".format(text[i]))
            i += 1
            if i >= len(text):
                break
            if text[i] == ' ':
                i += 1
            print("")
        print(f"{text[i]}", end="")
        i += 1
