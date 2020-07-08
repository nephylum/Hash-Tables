
def word_count(s):
    cache = {}
    s = s.lower()
    punctuation = '''!()-[]{};:"\|,+=<>./?@#$%^&*_~'''
    news = ""
    for char in s:
        if char not in punctuation:
            news += char

    print(news)
    listostrings=news.split()
    for item in listostrings:
        if item not in cache:
            cache[item] = 1
        else:
            cache[item] += 1
    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    
