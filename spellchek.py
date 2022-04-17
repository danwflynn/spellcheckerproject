# Daniel Flynn spell check class
from nltk.corpus import words
import itertools
import json


class SpellChek:
    def __init__(self, file):
        def valid_word(w):
            return w in words.words()\
                   or w[0:len(w)-2] + w[len(w)-2:len(w)-1].strip("ed") in words.words()\
                   or w[0:len(w)-1] + w[len(w)-1].strip("s") in words.words()\
                   or w[0:len(w)-2] + w[len(w)-2:len(w)-1].strip("'s") in words.words()\
                   or w[0:len(w)-2] + w[len(w)-2:len(w)-1].strip("s'") in words.words()\
                   or w[0:len(w)-3] + w[len(w)-3:len(w)-1].strip("n't") in words.words()

        self.file = file
        self.text = open(file, "r", encoding='utf-8')
        d = {}
        for line in self.text:
            line = line.strip()
            line = line.lower()
            xs = line.split(" ")
            for word in xs:
                word = word.strip(".")
                word = word.strip(",")
                word = word.strip("!")
                word = word.strip("?")
                word = word.strip("(")
                word = word.strip(")")
                word = word.strip("*")
                word = word.strip("[")
                word = word.strip("]")
                word = word.strip("{")
                word = word.strip("}")
                word = word.strip("0")
                word = word.strip("1")
                word = word.strip("2")
                word = word.strip("3")
                word = word.strip("4")
                word = word.strip("5")
                word = word.strip("6")
                word = word.strip("7")
                word = word.strip("8")
                word = word.strip("9")
                if len(word) > 0 and not valid_word(word):
                    fixes = []
                    for x in [''.join(p) for p in list(itertools.permutations(list(word)))][1:5]:
                        if len(x) > 0 and valid_word(x):
                            fixes.append(x)
                    d[word] = fixes
                    if len(d[word]) < 5:
                        for i in range(len(word)):
                            z = list(word)
                            z.pop(i)
                            if len(d[word]) < 5 and len(z) > 0 and valid_word("".join(z)) and "".join(z) not in d[word]:
                                d[word].append("".join(z))
                                break
                    if len(d[word]) < 5:
                        for i in range(len(word)):
                            z = list(word)
                            z.insert(i+1, z[i])
                            if len(d[word]) < 5 and len(z) > 0 and valid_word("".join(z)) and "".join(z) not in d[word]:
                                d[word].append("".join(z))
                                break
                    if len(d[word]) < 5 and len(word) == 9:
                        for i in range(len(word)):
                            z = list(word)
                            z.insert(i+1, " ")
                            y = "".join(z).split()
                            if len(d[word]) < 5 and len(z) > 0 and valid_word(y[0]) and valid_word(y[1])\
                                    and " ".join(y) not in d[word]:
                                d[word].append(" ".join(y))
                    if len(d[word]) == 0:
                        vowels = ['a', 'e', 'i', 'o', 'u']
                        for i in range(len(word)):
                            for a in vowels:
                                z = list(word)
                                z[i] = a
                                if len(d[word]) < 5 and len(z) > 0 and valid_word("".join(z))\
                                        and "".join(z) not in d[word]:
                                    d[word].append("".join(z))
        self.suggestions = d

    def ignore_all(self, word):
        word = word.lower()
        if word in self.suggestions.keys():
            self.suggestions.pop(word)
        else:
            print("Not found in suggestions")

    def __str__(self):
        return f'Suggestions:\n' \
               f'{json.dumps(self.suggestions, indent=len(self.suggestions))}'
