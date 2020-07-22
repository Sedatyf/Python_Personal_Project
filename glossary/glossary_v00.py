import os
import json
import re

quit = 0
file_path = os.path.join(os.path.dirname(__file__), "glossary.json")

if os.path.exists(file_path):
    with open(file_path, "r") as glossary_file:
        glossary_file = json.load(glossary_file)
else:
    glossary_file = {}

while quit == 0:
    print("""Choose an option :
    \t1: Add a word and a definition
    \t2: Remove a word and a definition
    \t3: Search for a definition
    \t4: Show all definitions
    \t5: Show help
    \t6: Quit""")
    try:
        user_nav = int(input())
    except ValueError:
        print("\nYou need to choose between option by typing the corresponding number\n")
        continue
    else:
        if user_nav == 1:
            add_quit = 0
            while add_quit == 0:
                new_word = input("Please type the word you want to add : ")
                if new_word in glossary_file:
                    print("This word is already in the glossary\n")
                    continue
                elif new_word == "cancel()":
                    print("Going back to main menu")
                    add_quit = 1
                else:
                    new_def = input("Please type the defition of your word : ")
                    glossary_file[new_word] = new_def
                    final_glossary = dict(sorted(glossary_file.items()))
                    add_quit = 1
        elif user_nav == 2:
            remove_quit = 0
            while remove_quit == 0:
                if len(glossary_file) > 0:
                    remove_word = input("Please type the word you want to remove : ")
                    if remove_word in glossary_file:
                        del glossary_file[remove_word]
                        final_glossary = dict(sorted(glossary_file.items()))
                        print("The word " + remove_word + " has been removed\n")
                        remove_quit = 1
                    elif remove_word == "cancel()":
                        print("Going back to main menu")
                        remove_quit = 1
                    else:
                        print("The word " + remove_word + " is not in the glossary")
                        continue
                else:
                    print("Nothing to remove : your glossary is empty")
                    remove_quit = 1
        elif user_nav == 3:
            search_word = input("Search the glossary : ")
            words_found = []
            for word in glossary_file:
                result = re.match(r"^"+search_word+"\w+", word)
                if result:
                    words_found.append(result.group(0))
            if len(words_found) > 0:
                print("Here the matched words : ")
                for word in words_found:
                    print(word + " : " + glossary_file[word])
            else:
                print("No match found")
        elif user_nav == 4:
            final_glossary = dict(sorted(glossary_file.items()))
            if len(final_glossary) > 0:
                print("These are the definitions in your glossary :")
                for word, definition in final_glossary.items():
                    print(word + " : " + definition)
            else:
                print("There is no word in your glossary")
        elif user_nav == 5:
            print("You can type \"cancel()\" when you're in option 1,2 or 3 to cancel action and go back to main menu")
        elif user_nav == 6:
            final_glossary = dict(sorted(glossary_file.items()))
            with open(file_path, "w") as save_file:
                json.dump(final_glossary, save_file, indent=4, ensure_ascii=False)
            quit = 1
        else:
            print("You need to choose a number between 1 to 5\n")