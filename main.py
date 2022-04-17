# Daniel Flynn Python Spell Checker main
from spellchek import SpellChek

menu = True
sct = SpellChek("spellcheckertest.txt")

print("Menu:\n"
      "1. Ignore a word\n"
      "2. Print suggestions\n"
      "3. Exit\n")

while menu:
    choice = int(input("Input a number (1-3): "))
    if choice == 1:
        sct.ignore_all(input("Ignore: "))
    elif choice == 2:
        print(sct)
    else:
        menu = False
