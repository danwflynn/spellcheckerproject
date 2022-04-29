from nltk.corpus import words
import itertools


class Suggester:
    def __init__(self, word):
        self.word = word
        self.options = []

    @staticmethod
    def valid_word(w):
        """
        Checks to see if a given string with no whitespace is a valid english word
        :param w: string
        :return: boolean
        """
        return w in words.words() \
            or w[0:len(w) - 2] + w[len(w) - 2:len(w) - 1].strip("ed") in words.words() \
            or w[0:len(w) - 1] + w[len(w) - 1].strip("s") in words.words() \
            or w[0:len(w) - 2] + w[len(w) - 2:len(w) - 1].strip("'s") in words.words() \
            or w[0:len(w) - 2] + w[len(w) - 2:len(w) - 1].strip("s'") in words.words() \
            or w[0:len(w) - 3] + w[len(w) - 3:len(w) - 1].strip("n't") in words.words()

    def get_permutations(self, a, b):
        for x in [''.join(p) for p in list(itertools.permutations(list(self.word)))][a:b]:
            if len(x) > 0 and Suggester.valid_word(x):
                self.options.append(x)

    def remove_extra_letters(self):
        for i in range(len(self.word)):
            z = list(self.word)
            z.pop(i)
            if len(z) > 0 and Suggester.valid_word("".join(z)) and "".join(z) not in self.options:
                self.options.append("".join(z))
                break

    def add_extra_letters(self):
        for i in range(len(self.word)):
            z = list(self.word)
            z.insert(i + 1, z[i])
            if len(z) > 0 and Suggester.valid_word("".join(z)) and "".join(z) not in self.options:
                self.options.append("".join(z))
                break

    def add_spaces(self):
        for i in range(len(self.word)):
            z = list(self.word)
            z.insert(i + 1, " ")
            y = "".join(z).split()
            if len(z) > 0 and Suggester.valid_word(y[0]) and Suggester.valid_word(y[1])\
                    and " ".join(y) not in self.options:
                self.options.append(" ".join(y))

    def add_vowels(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(self.word)):
            for a in vowels:
                z = list(self.word)
                z[i] = a
                if len(z) > 0 and Suggester.valid_word("".join(z)) and "".join(z) not in self.options:
                    self.options.append("".join(z))
