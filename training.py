import re
import argparse
from os import listdir as listdir
from sys import stdin as stdin
import pickle


def check(word=" "):
    if re.fullmatch('\W*', word) and not re.fullmatch('[.?!]+', word):
        return '', False

    elif re.fullmatch("\W*\w+[-']\w+\W*", word):
        return re.findall(r"\w+[-']\w+]", word), True

    elif re.fullmatch("\W*\w+\W*", word):
        return re.findall(r"\w+", word), True

    return word, False


words = {'.': {}}

parser = argparse.ArgumentParser(description='This program study. It gets text. '
                                             'Then it creates model - "small dictionary"')
parser.add_argument("--input-dir", action='store',
                    help="specify the path to the directory, where you have training files; default - stdin")
parser.add_argument("--model", action='store', nargs='?', default="model.txt",
                    help="specify the path to the file, where you want to save model")
parser.add_argument("--lc", action='store', type=bool, nargs='?', default=False,
                    help="leads words stored in the model to lower case")

arg = parser.parse_args()

if not (arg.input_dir is None):
    files = [x for x in listdir(path="{}".format(arg.input_dir)) if x.endswith(".txt")]
else:
    files = [""]

file = stdin
for f in files:
    if not (arg.input_dir is None):
        file = open("{}/{}".format(arg.input_dir, f), 'r')

    isEnd = False
    lastWord = "."
    for line in file:
        allWords = re.findall(r"[\w'-]+|[.?!]", line[:-1])

        for i in range(len(allWords)):
            w = allWords[i]
            if arg.lc:
                w = w.lower()

            w, result = check(w)
            if not w == '':
                if result:
                    if not(w in words.keys()):
                        words[w] = {}

                    if w in words[lastWord].keys():
                        words[lastWord][w] += 1
                    else:
                        words[lastWord][w] = 1

                elif not lastWord == '.':
                    if '.' in words[lastWord].keys():
                        words[lastWord]['.'] += 1
                    else:
                        words[lastWord]['.'] = 1
                    lastWord = '.'

    if not lastWord == '.' and not lastWord == '':
        if '.' in words[lastWord].keys():
            words[lastWord]['.'] += 1
        else:
            words[lastWord]['.'] = 1
        lastWord = '.'

file.close()

with open("{}".format(arg.model), 'wb') as outFile:
    pickle.dump(words, outFile)
