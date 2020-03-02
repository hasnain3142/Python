def wordgenerator():
    import random
    with open("words.txt") as file:
        s = file.read()
        words = s.split()
        nwords = len(words)
        SecretWord = random.choice(words)
    return SecretWord,nwords
