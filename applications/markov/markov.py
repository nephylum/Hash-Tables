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

#create function to create random sentences
def make_sentence(cache):
    # define the stop punctuation to finish a sentence
    stop = '.!?'
    new_sentence = ""
    # pick a random start word
    choices = list(cache.keys())
    choice = random.choice(choices)
    # print('choice:' , choice, '\nvalues:', cache[choice])
    #if it's a stop word, end sentence
    if choice[-1] in stop:
        new_sentence = choice

        return new_sentence
    # otherwise, pick random next word (from key's values)
    else:
        new_sentence = choice
        while len(new_sentence) > 0:
            choice= random.choice(cache[choice])
            if choice[-1] == '"':
                if choice[-2] in stop:
                    new_sentence += (" " + choice)
                    return new_sentence
            elif choice[-1] in stop:
                new_sentence += (' ' + choice)
                return new_sentence
            else:
                new_sentence += (" " + choice)

    return new_senctence

# construct 5 random sentences

print(make_sentence(cache), "\n")
print(make_sentence(cache), "\n")
print(make_sentence(cache), "\n")
print(make_sentence(cache), "\n")
print(make_sentence(cache))
