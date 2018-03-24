import re
import argparse
from os import listdir as listdir
from sys import stdin as stdin


def check(word=" "):
    word = word.lower()

    if re.fullmatch('[a-zа-я]*', word) or re.fullmatch("[0-9]*", word):
        return word, False, True

    elif re.fullmatch('[a-zа-я]*', word[:-1])\
            or re.fullmatch("[0-9]*", word[:-1]) and word[-1] == '.':
        return word[:-1], True, True

    elif re.fullmatch('[a-zа-я]*\W?', word) or re.fullmatch("[0-9]*\W?", word):
        return word[:-1], False, True

    elif re.fullmatch('[a-zа-я]*\W?', word[:-1])\
            or re.fullmatch("[0-9]*\W?", word[:-1]) and word[-1] == '.':
        return word[:-2], True, True

    elif re.fullmatch('[a-zа-я]*\W?\W?', word) or re.fullmatch("[0-9]*\W?\W?", word):
        return word[:-2], False, True

    elif re.fullmatch('[a-zа-я]*\W?\W?', word[:-1])\
            or re.fullmatch("[0-9]*\W?\W?", word[:-1]) and word[-1] == '.':
        return word[:-3], True, True

    ######################################################

    elif re.fullmatch("[a-z]*'[a-z]", word):
        return word, False, True

    elif re.fullmatch("[a-z]*'[a-z]", word[-1]) and word[-1] == '.':
        return word[:-1], True, True

    elif re.fullmatch("[a-z]*-[a-z]*", word):
        return word, False, True

    elif re.fullmatch("[a-z]*-[a-z]*", word[-1]) and word[-1] == '.':
        return word[:-1], True, True

    elif re.fullmatch("[a-z]*'[a-z]\W?", word):
        return word[:-1], False, True

    elif re.fullmatch("[a-z]*'[a-z]\W?", word[-1]) and word[-1] == '.':
        return word[:-2], True, True

    elif re.fullmatch("[a-z]*-[a-z]*\W?", word):
        return word[:-1], False, True

    elif re.fullmatch("[a-z]*-[a-z]*\W?", word[-1]) and word[-1] == '.':
        return word[:-2], True, True

    #######################################################

    elif re.fullmatch('\W?[a-zа-я]*', word) or re.fullmatch("\W?[0-9]*", word):
        return word[1:], False, True

    elif re.fullmatch('\W?[a-zа-я]*', word[:-1])\
            or re.fullmatch("\W?[0-9]*", word[:-1]) and word[-1] == '.':
        return word[1:-1], True, True

    elif re.fullmatch('\W?[a-zа-я]*\W?', word) or re.fullmatch("\W?[0-9]*\W?", word):
        return word[1:-1], False, True

    elif re.fullmatch('\W?[a-zа-я]*\W?', word[:-1])\
            or re.fullmatch("\W?[0-9]*\W?", word[:-1]) and word[-1] == '.':
        return word[1:-2], True, True

    elif re.fullmatch('\W?[a-zа-я]*\W?\W?', word) or re.fullmatch("\W?[0-9]*\W?\W?", word):
        return word[1:-2], False, True

    elif re.fullmatch('\W?[a-zа-я]*\W?\W?', word[:-1])\
            or re.fullmatch("\W?[0-9]*\W?\W?", word[:-1]) and word[-1] == '.':
        return word[1:-3], True, True

    ########################################################

    elif re.fullmatch("\W?[a-z]*'[a-z]", word):
        return word[1:], False, True

    elif re.fullmatch("\W?[a-z]*'[a-z]", word[-1]) and word[-1] == '.':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*", word):
        return word[1:], False, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*", word[-1]) and word[-1] == '.':
        return word[1:-1], True, True

    elif re.fullmatch("\W?[a-z]*'[a-z]\W?", word):
        return word[1:-1], False, True

    elif re.fullmatch("\W?[a-z]*'[a-z]\W?", word[-1]) and word[-1] == '.':
        return word[1:-2], True, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*\W?", word):
        return word[1:-1], False, True

    elif re.fullmatch("\W?[a-z]*-[a-z]*\W?", word[-1]) and word[-1] == '.':
        return word[1:-2], True, True



words = {}
words['.'] = {}

#argparse

directory = "" #something argparse
something = False #kind of input

if something:
    files = [x for x in listdir(path="{}".format(directory)) if x.endswith(".txt")]
else:
    files = [""]

for f in files:
    if something:
        file = open("{}".format(f), 'r')
    else:
        file = stdin

    isEnd = False
    lastWord = "."
    while True:
        try:
            allWords = input().split()

            for i in range(len(allWords)):
                w = allWords[i]

                w, isEnd, result = check(w)
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
                else:
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
#output