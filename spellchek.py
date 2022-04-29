# Daniel Flynn spell check class
from suggester import Suggester
import json
import random
import math


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
                word = word.strip("$")
                if 0 < len(word) < 3 and not Suggester.valid_word(word):
                    typo = Suggester(word)
                    typo.get_permutations(1, 2)
                    if len(word) == 2 and len(typo.options) < 5:
                        typo.remove_extra_letters()
                    if len(typo.options) < 5:
                        typo.add_extra_letters()
                    if len(typo.options) < 5:
                        typo.add_spaces()
                    self.suggestions[word] = typo.options
                elif len(word) > 0 and not Suggester.valid_word(word):
                    typo = Suggester(word)
                    typo.get_permutations(1, 3)
                    if len(typo.options) < 3:
                        typo.remove_extra_letters()
                    if len(typo.options) < 3:
                        typo.add_extra_letters()
                    if len(typo.options) < 3:
                        typo.add_spaces()
                    if len(typo.options) == 0:
                        typo.add_vowels()
                    self.suggestions[word] = typo.options

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
            typo = Suggester(word)
            r = random.randint(5, math.factorial(len(word)) - 5)
            typo.get_permutations(r, r+5)
            typo.remove_extra_letters()
            typo.add_extra_letters()
            typo.add_spaces()
            typo.add_vowels()
            self.suggestions[word] = typo.options
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
                    elif word.strip(".") in self.corrections.keys():
                        o.append(self.corrections[word.strip(".")] + ".")
                    elif word.strip(".").lower() in self.corrections.keys():
                        o.append(self.corrections[word.strip(".").lower()].capitalize() + ".")
                    elif word.strip(",") in self.corrections.keys():
                        o.append(self.corrections[word.strip(",")] + ",")
                    elif word.strip(",").lower() in self.corrections.keys():
                        o.append(self.corrections[word.strip(",").lower()].capitalize() + ",")
                    elif word.strip("!") in self.corrections.keys():
                        o.append(self.corrections[word.strip("!")] + "!")
                    elif word.strip("!").lower() in self.corrections.keys():
                        o.append(self.corrections[word.strip("!").lower()].capitalize() + "!")
                    elif word.strip("?") in self.corrections.keys():
                        o.append(self.corrections[word.strip("?")] + "?")
                    elif word.strip("?").lower() in self.corrections.keys():
                        o.append(self.corrections[word.strip("?").lower()].capitalize() + "?")
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
