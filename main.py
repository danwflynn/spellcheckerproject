# Daniel Flynn Python Spell Checker main
from spellchek import SpellChek
from menu import Menu

filename = input("Filename: ")
Menu.loading_screen()
sct = SpellChek(filename)
Menu.display_menu()
Menu.implement_choices(sct)

# Important things to note:
# Initializing SpellChek object may take up to 90 seconds due to magnitude of operations performed
# Because of this same reason, refreshing suggestions may take up to 10 seconds
