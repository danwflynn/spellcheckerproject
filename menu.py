from spellchek import SpellChek
import sys
import time


class Menu:
    @staticmethod
    def loading_screen():
        """
        Displays loading screen before initializing spellchek variable
        :return:
        """
        a = 0
        for x in range(0, 5):
            a = a + 1
            b = ("Loading" + "." * a)
            sys.stdout.write('\r' + b)
            time.sleep(0.5)

    @staticmethod
    def display_menu():
        """
        Displays menu after spellchek variable is loaded
        :return:
        """
        sys.stdout.write('\r')
        print("Menu:\n"
              "1. Ignore a word\n"
              "2. Print suggestions and corrections\n"
              "3. Refresh suggestions for a given word\n"
              "4. Get corrections from user\n"
              "5. Make corrections to document\n"
              "6. Print the document\n"
              "7. Exit\n")

    @staticmethod
    def implement_choices(v):
        """
        Uses infinite while loop to implement choices that correspond to spellchek methods
        :param v:
        :return:
        """
        while True:
            choice = int(input("Input a number (1-7): "))
            if choice == 1:
                v.ignore_all(input("Ignore: "))
            elif choice == 2:
                print(v)
            elif choice == 3:
                v.refresh_suggestions(input("Refresh: "))
            elif choice == 4:
                v.get_corrections_from_user()
            elif choice == 5:
                v.make_corrections()
            elif choice == 6:
                v.print_doc()
                print()
            elif choice == 7:
                break
