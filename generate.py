import pickle
import random

file = open('model.txt', 'rb')
words = pickle.load(file)

file = open("text.txt", 'w')

n = int(input())
currentWord = '.'
for i in range(n):
    nextWords = []
    for w in words[currentWord]:
        for j in range(words[currentWord][w]):
            nextWords.append(w)
    word = random.choice(nextWords)
    if currentWord == '.':
        word = word.capitalize()
    if len(words[word.lower()]) == 0:
        print(" {}.".format(word), end='', sep='')
        currentWord = '.'
    elif word == '.':
        print(".", end='', sep='')
        currentWord = '.'
    else:
        print(" {}".format(word), end='', sep='')
        currentWord = word.lower()
