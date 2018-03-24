import pickle
from random import choice as choice
from sys import stdout as stdout
import argparse

parser = argparse.ArgumentParser(description='This program generate new text based on given model')
parser.add_argument("--model", action='store', nargs='?', default="model.txt",
                    help="specify the path to the directory, where you have model")
parser.add_argument("--seed", action='store', nargs='?', default='.',
                    help="if you want, specify the first word")
parser.add_argument("--output", action='store',
                    help="specify the path to the file, where you want to save model; default - stdout")
parser.add_argument("--length", action='store', type=int, required=True,
                    help="specify the length(count of words) of generated text")

arg = parser.parse_args()

file = open('{}'.format(arg.model), 'rb')
words = pickle.load(file)

file = stdout
if not (arg.output is None):
    file = open("{}".format(arg.output), 'w')

n = arg.length
currentWord = arg.seed
for i in range(n):
    nextWords = []
    for w in words[currentWord]:
        for j in range(words[currentWord][w]):
            nextWords.append(w)
    word = choice(nextWords)
    if len(words[word]) == 0:
        if currentWord == '.':
            word = word[0].upper() + w[1:]
        print(" {}.".format(word), end='', sep='')
        currentWord = '.'
    elif word == '.':
        print(".", end='', sep='')
        currentWord = '.'
    else:
        currentWord = word
        if currentWord == '.':
            word = word[0].upper() + w[1:]
        print(" {}".format(word), end='', sep='')
