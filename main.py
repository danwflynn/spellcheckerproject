# Daniel Flynn Python Spell Checker main
from spellchek import SpellChek

menu = True
sct = SpellChek("spellcheckertest.txt")

print("Menu:\n"
      "1. Ignore a word\n"
      "2. Print suggestions and corrections\n"
      "3. Refresh suggestions for a given word\n"
      "4. Get corrections from user\n"
      "5. Make corrections to document\n"
      "6. Print the document\n"
      "7. Exit\n")

while menu:
    choice = int(input("Input a number (1-7): "))
    if choice == 1:
        sct.ignore_all(input("Ignore: "))
    elif choice == 2:
        print(sct)
    elif choice == 3:
        sct.refresh_suggestions(input("Refresh: "))
    elif choice == 4:
        sct.get_corrections_from_user()
    elif choice == 5:
        sct.make_corrections()
    elif choice == 6:
        sct.print_doc()
        print()
    elif choice == 7:
        menu = False
