import os, glob
import termcolor, tqdm
import custom_tools

#Global variable
given = []
when = []
then = []

is_feature_folder_find = False
is_step_folder_find = False

#Script
while not is_feature_folder_find:
    filepath_feature = input("Veuillez préciser le chemin du dossier contenant les fichiers .features : ")
    is_feature_folder_find =  custom_tools.check_folder(filepath_feature)
while not is_step_folder_find:
    filepath_steps = input("Veuillez préciser le chemin du dossier contenant les fichiers java : ")
    is_step_folder_find = custom_tools.check_folder(filepath_steps)

custom_tools.parse_feature_file(filepath_feature, given, when, then)
custom_tools.write_in_file(filepath_steps, given, when, then)
termcolor.cprint("Tous les tests ont été traités !", "green")
