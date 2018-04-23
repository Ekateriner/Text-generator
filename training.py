import re
import argparse
from os import listdir as listdir
from sys import stdin as stdin
import pickle


def check(word=" "):
    
    #
    # первое возвращается слово или то что считалось словом или '', в зависимости от этого
    # мы либо будем обрабатывать его, либо считать что цепочка слов закончилась, либо игнорим
    # так как по возвращаемому значению не понятно слово ли это, возвращаем также bool
    #

    if re.fullmatch('\W*', word) and not re.fullmatch('[.?!]+', word):
        return '', False

    #
    # так как re.fullmatch ниже возвращает list (хотя он и состоит из одного слова) пишу [0]
    #

    elif re.fullmatch("\W*\w+[-']\w+\W*", word):
        return re.findall(r"\w+[-']\w+", word)[0], True

    elif re.fullmatch("\W*\w+\W*", word):
        return re.findall("\w+", word)[0], True

    return word, False


def new_open(arg_file='', directory=None):
    if directory is None:
        file = stdin
    else:
        file = open("{dir}/{file_name}".format(dir=directory, file_name=arg_file), 'r')
    
    try:
        yield file
    finally:
        if file is not stdin:
            file.close()


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

for f in files:
    with new_open(f, arg.input_dir) as file:
        isEnd = False
        lastWord = "."
        for line in file:
            allWords = re.findall(r"[\w'-]+|[.?!]|\n", line[:-1])

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

                        lastWord = w

                    elif lastWord != '.':
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

with open("{}".format(arg.model), 'wb') as outFile:
    pickle.dump(words, outFile)
