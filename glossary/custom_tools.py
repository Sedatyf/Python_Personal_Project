import os
import json
import re

# Functions
def check_file_exists(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as glossary_file:
            return json.load(glossary_file)

def print_menu():
    print("""Choose an option :
    \t1: Add a word and a definition
    \t2: Remove a word and a definition
    \t3: Search for a definition
    \t4: Show all definitions
    \t5: Show help
    \t6: Quit""")

def add_word(glossary_file):
    add_quit = 0
    while add_quit == 0:
        new_word = input("Please type the word you want to add : ").title()
        if new_word in glossary_file:
            print("This word is already in the glossary\n")
            continue
        elif new_word.lower() == "cancel()":
            print("Going back to main menu")
            add_quit = 1
        else:
            new_def = input("Please type the defition of your word : ")
            glossary_file[new_word] = new_def
            add_quit = 1
            return dict(sorted(glossary_file.items()))

def remove_word(glossary_file):
    remove_quit = 0
    while remove_quit == 0:
        if len(glossary_file) > 0:
            remove_word = input("Please type the word you want to remove : ").title()
            if remove_word in glossary_file:
                del glossary_file[remove_word]
                print("The word " + remove_word + " has been removed\n")
                remove_quit = 1
                return dict(sorted(glossary_file.items()))
            elif remove_word.lower() == "cancel()":
                print("Going back to main menu")
                remove_quit = 1
            else:
                print("The word " + remove_word + " is not in the glossary")
                continue
        else:
            print("Nothing to remove : your glossary is empty")
            remove_quit = 1

def search_word(glossary_file):
    search_word = input("Search the glossary : ").title()
    words_found = []
    for word in glossary_file:
        result = re.match(r"^"+search_word+"\w+", word)
        if result:
            words_found.append(result.group(0))
    if words_found:
        print("Here the matched words : ")
        for word in words_found:
            print(word + " : " + glossary_file[word])
        print("\b")
    else:
        print("No match found")

def show_words(glossary_file):
    final_glossary = dict(sorted(glossary_file.items()))
    if final_glossary:
        print("These are the definitions in your glossary :")
        print("\b")
        for word, definition in final_glossary.items():
            print(word + " : " + definition)
            print("\b")
    else:
        print("There is no word in your glossary")

def save_words(glossary_file, file_path):
    final_glossary = dict(sorted(glossary_file.items()))
    with open(file_path, "w") as save_file:
        json.dump(final_glossary, save_file, indent=4, ensure_ascii=False)
        quit = 1
    return quit
