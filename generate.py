import pickle
from random import choice as choice
from sys import stdout as stdout
import argparse

def new_open(arg_file=None):
    if arg_file is None:
        file = stdout
    else:
        file = open("{file_name}".format(file_name=arg_file), 'w')
    
    try:
        yield file
    finally:
        if file is not stdin:
            file.close()


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

with open('{}'.format(arg.model), 'rb') as file:
    words = pickle.load(file)

with new_open(arg.output) as file:
    n = arg.length
    currentWord = arg.seed
    for i in range(n):
        nextWords = []
        for w in words[currentWord]:
            for j in range(words[currentWord][w]):
                nextWords.append(w)
        word = choice(nextWords)
        if word == '.':
            file.write(".")
            currentWord = '.'
        elif len(words[word]) == 0:
            if currentWord == '.':
                word = word[0].upper() + word[1:]
            file.write(" {}".format(word))
            file.write(".")
            currentWord = '.'
        else:
            if currentWord == '.':
                currentWord = word
                word = word[0].upper() + word[1:]
            else:
                currentWord = word
            file.write(" {}".format(word))

