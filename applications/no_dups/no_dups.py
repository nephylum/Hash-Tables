def no_dups(s):
    # Implement me.
    cache = {}
    listowords = s.split()
    str_out = ""
    for word in listowords:
        if word not in cache:
            if len(str_out)==0:
                str_out += word
            else:
                str_out += " " + word
            cache[word] = 1
    return str_out

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
