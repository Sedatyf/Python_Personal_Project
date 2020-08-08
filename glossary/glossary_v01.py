import os
import custom_tools as ct

# Global variables
quit = 0
file_path = os.path.join(os.path.dirname(__file__), "glossary.json")
glossary_file = {}
final_glossary = {}

# Script
glossary_file = ct.check_file_exists(file_path)

while quit == 0:
    ct.print_menu()
    try:
        user_nav = int(input())
    except ValueError:
        print("\nYou need to choose between option by typing the corresponding number\n")
        continue
    else:
        if user_nav == 1:
            final_glossary = ct.add_word(glossary_file)
        elif user_nav == 2:
            final_glossary = ct.remove_word(glossary_file)
        elif user_nav == 3:
            ct.search_word(glossary_file)
        elif user_nav == 4:
            ct.show_words(glossary_file)
        elif user_nav == 5:
            print("You can type \"cancel()\" when you're in option 1 or 2 to cancel action and go back to main menu")
        elif user_nav == 6:
            quit = ct.save_words(glossary_file, file_path)
        else:
            print("You need to choose a number between 1 to 5\n")
