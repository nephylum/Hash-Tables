import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
listowords = words.split()
#print(listowords)

# TODO: analyze which words can follow other words

cache = {}
for x in range(len(listowords)):
# if word doesn't exist in cache, create a new word and assign the next word
# as the key value
    if listowords[x] not in cache:
        if x < len(listowords) - 1:
            cache[listowords[x]] = [listowords[x + 1]]
        else:
            cache[listowords[x]] = ""
    elif listowords[x] in cache:
        if x < len(listowords) - 1:
            cache[listowords[x]].append(listowords[x + 1])
print(len(cache['the']))

# TODO: construct 5 random sentences
