import re
import argparse
from os import listdir as listdir
from sys import stdin as stdin
import pickle


def check(word=" ", lc=False):
    if lc:
        word = word.lower()

    if re.fullmatch('[a-zа-я]*', word) or re.fullmatch("[0-9]*", word):
        return word, False, True

    elif (re.fullmatch('[a-zа-я]*', word[:-1])
            or re.fullmatch("[0-9]*", word[:-1])) and word[-1] == '.':
        return word[:-1], True, True

    elif (re.fullmatch('[a-zа-я]*', word[:-1])
            or re.fullmatch("[0-9]*", word[:-1])) and word[-1] == '!':
        return word[:-1], True, True

    elif (re.fullmatch('[a-zа-я]*', word[:-1])
            or re.fullmatch("[0-9]*", word[:-1])) and word[-1] == '?':
        return word[:-1], True, True

    elif re.fullmatch("[a-z]*'", word):
        return word, False, True

    elif re.fullmatch("[0-9]*1st", word) or re.fullmatch("[0-9]*2nd", word) \
            or re.fullmatch("[0-9]*3rd", word) or re.fullmatch("[0-9]*th", word):
        return word, False, True

    elif re.fullmatch('[a-zа-я]*\W?', word) or re.fullmatch("[0-9]*\W?", word):
        return word[:-1], False, True

    elif (re.fullmatch('[a-zа-я]*\W?', word[:-1])
            or re.fullmatch("[0-9]*\W?", word[:-1])) and word[-1] == '.':
        return word[:-2], True, True

    elif (re.fullmatch('[a-zа-я]*\W?', word[:-1])
            or re.fullmatch("[0-9]*\W?", word[:-1])) and word[-1] == '!':
        return word[:-2], True, True

    elif (re.fullmatch('[a-zа-я]*\W?', word[:-1])
            or re.fullmatch("[0-9]*\W?", word[:-1])) and word[-1] == '?':
        return word[:-2], True, True

    elif re.fullmatch('[a-zа-я]*\W?\W?', word) or re.fullmatch("[0-9]*\W?\W?", word):
        return word[:-2], False, True

    elif (re.fullmatch('[a-zа-я]*\W?\W?', word[:-1])
            or re.fullmatch("[0-9]*\W?\W?", word[:-1])) and word[-1] == '.':
        return word[:-3], True, True

    elif (re.fullmatch('[a-zа-я]*\W?\W?', word[:-1])
            or re.fullmatch("[0-9]*\W?\W?", word[:-1])) and word[-1] == '!':
        return word[:-3], True, True

    elif (re.fullmatch('[a-zа-я]*\W?\W?', word[:-1])
            or re.fullmatch("[0-9]*\W?\W?", word[:-1])) and word[-1] == '?':
        return word[:-3], True, True

    ######################################################

    elif re.fullmatch("[a-z]*'[a-z]", word):
        return word, False, True

    elif re.fullmatch("[a-z]*'[a-z]", word[-1]) and word[-1] == '.':
        return word[:-1], True, True

    elif re.fullmatch("[a-z]*'[a-z]", word[-1]) and word[-1] == '!':
        return word[:-1], True, True

    elif re.fullmatch("[a-z]*'[a-z]", word[-1]) and word[-1] == '?':
        return word[:-1], True, True

    elif re.fullmatch("[a-zа-я]*-[a-zа-я]*", word):
        return word, False, True

    elif re.fullmatch("[a-zа-я]*-[a-zа-я]*", word[-1]) and word[-1] == '.':
        return word[:-1], True, True

    elif re.fullmatch("[a-zа-я]*-[a-zа-я]*", word[-1]) and word[-1] == '!':
        return word[:-1], True, True

    elif re.fullmatch("[a-zа-я]*-[a-zа-я]*", word[-1]) and word[-1] == '?':
        return word[:-1], True, True

    elif re.fullmatch("[a-z]*'[a-z]\W?", word):
        return word[:-1], False, True

    elif re.fullmatch("[a-z]*'[a-z]\W?", word[-1]) and word[-1] == '.':
        return word[:-2], True, True

    elif re.fullmatch("[a-z]*-[a-z]*\W?", word):
        return word[:-1], False, True

    elif re.fullmatch("[a-zа-я]*-[a-zа-я]*\W?", word[-1]) and word[-1] == '.':
        return word[:-2], True, True

    elif re.fullmatch("[a-zа-я]*-[a-zа-я]*\W?", word[-1]) and word[-1] == '!':
        return word[:-2], True, True

    elif re.fullmatch("[a-zа-я]*-[a-zа-я]*\W?", word[-1]) and word[-1] == '?':
        return word[:-2], True, True

    ######################################################

    elif re.fullmatch("[a-zа-я]*-[0-9]*", word):
        return word, False, True

    elif re.fullmatch("[a-zа-я]*-[0-9]*", word[-1]) and word[-1] == '.':
        return word[:-1], True, True

    elif re.fullmatch("[a-zа-я]*-[0-9]*", word[-1]) and word[-1] == '!':
        return word[:-1], True, True

    elif re.fullmatch("[a-zа-я]*-[0-9]*", word[-1]) and word[-1] == '?':
        return word[:-1], True, True

    elif re.fullmatch("[a-zа-я]*-[0-9]*\W?", word):
        return word[:-1], False, True

    elif re.fullmatch("[a-zа-я]*-[0-9]*\W?", word[-1]) and word[-1] == '.':
        return word[:-2], True, True

    elif re.fullmatch("[a-zа-я]*-[0-9]*\W?", word[-1]) and word[-1] == '!':
        return word[:-2], True, True

    elif re.fullmatch("[a-zа-я]*-[0-9]*\W?", word[-1]) and word[-1] == '?':
        return word[:-2], True, True

    #######################################################

    elif re.fullmatch('\W?[a-zа-я]*', word) or re.fullmatch("\W?[0-9]*", word):
        return word[1:], False, True

    elif (re.fullmatch('\W?[a-zа-я]*', word[:-1])
            or re.fullmatch("\W?[0-9]*", word[:-1])) and word[-1] == '.':
        return word[1:-1], True, True

    elif (re.fullmatch('\W?[a-zа-я]*', word[:-1])
            or re.fullmatch("\W?[0-9]*", word[:-1])) and word[-1] == '!':
        return word[1:-1], True, True

    elif (re.fullmatch('\W?[a-zа-я]*', word[:-1])
            or re.fullmatch("\W?[0-9]*", word[:-1])) and word[-1] == '?':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-z]*'", word):
        return word[1:], False, True

    elif re.fullmatch("\W?[0-9]*1st", word) or re.fullmatch("\W?[0-9]*2nd", word) \
            or re.fullmatch("\W?[0-9]*3rd", word) or re.fullmatch("\W?[0-9]*th", word):
        return word[1:], False, True

    elif re.fullmatch('\W?[a-zа-я]*\W?', word) or re.fullmatch("\W?[0-9]*\W?", word):
        return word[1:-1], False, True

    elif (re.fullmatch('\W?[a-zа-я]*\W?', word[:-1])
            or re.fullmatch("\W?[0-9]*\W?", word[:-1])) and word[-1] == '.':
        return word[1:-2], True, True

    elif (re.fullmatch('\W?[a-zа-я]*\W?', word[:-1])
            or re.fullmatch("\W?[0-9]*\W?", word[:-1])) and word[-1] == '!':
        return word[1:-2], True, True

    elif (re.fullmatch('\W?[a-zа-я]*\W?', word[:-1])
            or re.fullmatch("\W?[0-9]*\W?", word[:-1])) and word[-1] == '?':
        return word[1:-2], True, True

    elif re.fullmatch('\W?[a-zа-я]*\W?\W?', word) or re.fullmatch("\W?[0-9]*\W?\W?", word):
        return word[1:-2], False, True

    elif re.fullmatch('\W?[a-zа-я]*\W?\W?', word[:-1])\
            or re.fullmatch("\W?[0-9]*\W?\W?", word[:-1]) and word[-1] == '.':
        return word[1:-3], True, True

    elif (re.fullmatch('\W?[a-zа-я]*\W?\W?', word[:-1])
            or re.fullmatch("\W?[0-9]*\W?\W?", word[:-1])) and word[-1] == '!':
        return word[1:-3], True, True

    elif (re.fullmatch('\W?[a-zа-я]*\W?\W?', word[:-1])
            or re.fullmatch("\W?[0-9]*\W?\W?", word[:-1])) and word[-1] == '?':
        return word[1:-3], True, True

    ########################################################

    elif re.fullmatch("\W?[a-z]*'[a-z]", word):
        return word[1:], False, True

    elif re.fullmatch("\W?[a-z]*'[a-z]", word[-1]) and word[-1] == '.':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-z]*'[a-z]", word[-1]) and word[-1] == '!':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-z]*'[a-z]", word[-1]) and word[-1] == '?':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[a-zа-я]*", word):
        return word[1:], False, True

    elif re.fullmatch("\W?[a-zа-я]*-[a-zа-я]*", word[-1]) and word[-1] == '.':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[a-zа-я]*", word[-1]) and word[-1] == '!':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[a-zа-я]*", word[-1]) and word[-1] == '?':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-z]*'[a-z]\W?", word):
        return word[1:-1], False, True

    elif re.fullmatch("\W?[a-z]*'[a-z]\W?", word[-1]) and word[-1] == '.':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-z]*'[a-z]\W?", word[-1]) and word[-1] == '!':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-z]*'[a-z]\W?", word[-1]) and word[-1] == '?':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*\W?", word):
        return word[1:-1], False, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*\W?", word[-1]) and word[-1] == '.':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*\W?", word[-1]) and word[-1] == '?':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*\W?", word[-1]) and word[-1] == '!':
        return word[1:-2], True, True

    ######################################################

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*", word):
        return word[1:], False, True

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*", word[-1]) and word[-1] == '.':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*", word[-1]) and word[-1] == '!':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*", word[-1]) and word[-1] == '?':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*\W?", word):
        return word[1:-1], False, True

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*\W?", word[-1]) and word[-1] == '.':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*\W?", word[-1]) and word[-1] == '!':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-zа-я]*-[0-9]*\W?", word[-1]) and word[-1] == '?':
        return word[1:-2], True, True

    return '', False, False


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
        file = open("{}".format(f), 'r')

    isEnd = False
    lastWord = "."
    while True:
        try:
            allWords = input().split()

            if (arg.input_dir is None) and allWords == ["0"]:
                break

            for i in range(len(allWords)):
                w = allWords[i]

                w, isEnd, result = check(w, arg.lc)
                if result:
                    if not(w in words.keys()):
                        words[w] = {}

                    if w in words[lastWord].keys():
                        words[lastWord][w] += 1
                    else:
                        words[lastWord][w] = 1

                    if isEnd:
                        if '.' in words[w].keys():
                            words[w]['.'] += 1
                        else:
                            words[w]['.'] = 1
                        lastWord = '.'
                    else:
                        lastWord = w
                elif not lastWord == '.':
                    if '.' in words[lastWord].keys():
                        words[lastWord]['.'] += 1
                    else:
                        words[lastWord]['.'] = 1
                    lastWord = '.'

        except EOFError:
            break

    if lastWord != '.':
        if '.' in words[lastWord].keys():
            words[lastWord]['.'] += 1
        else:
            words[lastWord]['.'] = 1
        lastWord = '.'

outFile = open("{}".format(arg.model), 'wb')
pickle.dump(words, outFile)
