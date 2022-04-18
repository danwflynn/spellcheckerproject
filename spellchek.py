# Daniel Flynn spell check class
from nltk.corpus import words
import itertools
import json
import random
import math


def valid_word(w):
    """
    Checks to see if a given string with no whitespace is a valid english word
    :param w: string
    :return: boolean
    """
    return w in words.words() \
        or w[0:len(w)-2] + w[len(w)-2:len(w)-1].strip("ed") in words.words() \
        or w[0:len(w)-1] + w[len(w)-1].strip("s") in words.words() \
        or w[0:len(w)-2] + w[len(w)-2:len(w)-1].strip("'s") in words.words() \
        or w[0:len(w)-2] + w[len(w)-2:len(w)-1].strip("s'") in words.words() \
        or w[0:len(w)-3] + w[len(w)-3:len(w)-1].strip("n't") in words.words()


class SpellChek:
    def __init__(self, file):
        """
        Initializes spell check object
        :param file: Filename as a string
        """
        self.file = file
        self.text = open(file, "r", encoding='utf-8')
        self.suggestions = {}
        self.corrections = {}
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
                if 0 < len(word) < 3 and not valid_word(word):
                    fixes = []
                    for x in [''.join(p) for p in list(itertools.permutations(list(word)))]:
                        if len(x) > 0 and valid_word(x):
                            fixes.append(x)
                    self.suggestions[word] = fixes
                    if len(self.suggestions[word]) < 5:
                        for i in range(len(word)):
                            z = list(word)
                            z.insert(i+1, " ")
                            y = "".join(z).split()
                            if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word(y[0])\
                                    and valid_word(y[1]) and " ".join(y) not in self.suggestions[word]:
                                self.suggestions[word].append(" ".join(y))
                    if len(self.suggestions[word]) == 0:
                        vowels = ['a', 'e', 'i', 'o', 'u']
                        for i in range(len(word)):
                            for a in vowels:
                                z = list(word)
                                z[i] = a
                                if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word("".join(z)) \
                                        and "".join(z) not in self.suggestions[word]:
                                    self.suggestions[word].append("".join(z))
                elif len(word) > 0 and not valid_word(word):
                    fixes = []
                    for x in [''.join(p) for p in list(itertools.permutations(list(word)))][1:5]:
                        if len(x) > 0 and valid_word(x):
                            fixes.append(x)
                    self.suggestions[word] = fixes
                    if len(self.suggestions[word]) < 5:
                        for i in range(len(word)):
                            z = list(word)
                            z.pop(i)
                            if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word("".join(z)) and "".join(z)\
                                    not in self.suggestions[word]:
                                self.suggestions[word].append("".join(z))
                                break
                    if len(self.suggestions[word]) < 5:
                        for i in range(len(word)):
                            z = list(word)
                            z.insert(i+1, z[i])
                            if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word("".join(z)) and "".join(z)\
                                    not in self.suggestions[word]:
                                self.suggestions[word].append("".join(z))
                                break
                    if len(self.suggestions[word]) < 5 and len(word) > 8:
                        for i in range(len(word)):
                            z = list(word)
                            z.insert(i+1, " ")
                            y = "".join(z).split()
                            if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word(y[0])\
                                    and valid_word(y[1]) and " ".join(y) not in self.suggestions[word]:
                                self.suggestions[word].append(" ".join(y))
                    if len(self.suggestions[word]) == 0:
                        vowels = ['a', 'e', 'i', 'o', 'u']
                        for i in range(len(word)):
                            for a in vowels:
                                z = list(word)
                                z[i] = a
                                if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word("".join(z)) \
                                        and "".join(z) not in self.suggestions[word]:
                                    self.suggestions[word].append("".join(z))

    def print_doc(self):
        """
        Method to print the text document that the object contains
        :return:
        """
        with open(self.file, encoding='utf8') as f:
            for line in f:
                print(line, end='')

    def ignore_all(self, word):
        """
        Removes word from suggestions
        :param word: String
        :return:
        """
        word = word.lower()
        if word in self.suggestions.keys():
            self.suggestions.pop(word)
        else:
            print("Not found in suggestions")

    def refresh_suggestions(self, word):
        """
        Gives new random valid suggestions for a given word
        :param word: String
        :return:
        """
        if word in self.suggestions.keys() and len(word) > 3:
            fixes = []
            r = random.randint(5, math.factorial(len(word)) - 5)
            for x in [''.join(p) for p in list(itertools.permutations(list(word)))][r:r+5]:
                if len(x) > 0 and valid_word(x):
                    fixes.append(x)
            self.suggestions[word] = fixes
            if len(self.suggestions[word]) < 5:
                for i in range(len(word)):
                    z = list(word)
                    z.pop(i)
                    if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word("".join(z))\
                            and "".join(z) not in self.suggestions[word]:
                        self.suggestions[word].append("".join(z))
            if len(self.suggestions[word]) < 5:
                for i in range(len(word)):
                    z = list(word)
                    z.insert(i + 1, z[i])
                    if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word("".join(z))\
                            and "".join(z) not in self.suggestions[word]:
                        self.suggestions[word].append("".join(z))
            if len(self.suggestions[word]) < 5 and len(word) > 8:
                for i in range(len(word)):
                    z = list(word)
                    z.insert(i + 1, " ")
                    y = "".join(z).split()
                    if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word(y[0]) and valid_word(y[1]) \
                            and " ".join(y) not in self.suggestions[word]:
                        self.suggestions[word].append(" ".join(y))
            if len(self.suggestions[word]) < 5:
                vowels = ['a', 'e', 'i', 'o', 'u']
                for i in range(len(word)):
                    for a in vowels:
                        z = list(word)
                        z[i] = a
                        if len(self.suggestions[word]) < 5 and len(z) > 0 and valid_word("".join(z)) \
                                and "".join(z) not in self.suggestions[word]:
                            self.suggestions[word].append("".join(z))
        else:
            print("Word must be present in document and have over 3 characters")

    def get_corrections_from_user(self):
        """
        Allows user to choose corrections from suggestions dictionary
        :return:
        """
        print("Enter 0 when done")
        while True:
            if self.corrections.keys() == self.suggestions.keys():
                break
            word = input("Word to be corrected (or 0): ")
            if word == "0":
                break
            if word in self.suggestions.keys():
                while True:
                    correction = input("Correction: ")
                    if correction in self.suggestions[word]:
                        self.corrections[word] = correction
                        break
                    else:
                        print("Not in suggestions dictionary")
            else:
                print("Not in suggestions dictionary")

    def make_corrections(self):
        """
        Applies corrections given by the user to the file itself
        :return:
        """
        c = []
        with open(self.file, encoding='utf8') as f:
            for line in f:
                o = []
                for word in line.split(" "):
                    if word in self.corrections.keys():
                        o.append(self.corrections[word])
                    elif word.lower() in self.corrections.keys():
                        o.append(self.corrections[word.lower()].capitalize())
                    else:
                        o.append(word)
                c.append(" ".join(o))
        with open(self.file, 'w', encoding='utf8') as f:
            f.truncate()
            for line in c:
                f.write(line)

    def __str__(self):
        """
        Method for printing object data
        :return: String
        """
        return f'Suggestions:\n' \
               f'{json.dumps(self.suggestions, indent=len(self.suggestions))}\n' \
               f'Corrections:\n' \
               f'{json.dumps(self.corrections, indent=len(self.corrections))}'
