import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
listowords = words.split()
#print(listowords)
cache = {}
for x in range(len(listowords)):
    if x < len(listowords) - 1:
        cache[listowords[x]] += listowords[x + 1]

print(cache)

# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences
