import os
import termcolor
import glob

#Global variable
given = []
when = []
then = []

is_feature_folder_find = False
is_step_folder_find = False

#Functions
def check_folder(filepath):
    if os.path.exists(filepath):
        termcolor.cprint("Dossier trouvé !", "green")
        return True
    else:
        termcolor.cprint("Dossier non trouvé !", "red")
        return False

def parse_feature_file(feature_folder):
    #TODO arriver à récupérer les and et les mettre dans la bonne liste.
    #TODO corriger les feature files, bug chelou
    for feature_file in glob.glob(os.path.join(feature_folder, "*.feature")):
        with open(feature_file, "r") as open_file:
            current_feature = open_file.readlines()
        processed_lines = [x.replace("\n", "") for x in current_feature if x.startswith("Given") or x.startswith("When") or x.startswith("Then") or x.startswith("And")]
        for line in processed_lines:
            if line.startswith("Given"):
                given.append(line)
            elif line.startswith("When"):
                when.append(line)
            elif line.startswith("Then"):
                then.append(line)
        print(f"Given : {given}")
        print(f"When : {when}")
        print(f"Then : {then}")

#Script
while is_feature_folder_find == False:
    filepath_feature = input("Veuillez préciser le chemin du dossier contenant les fichiers .features : ")
    is_feature_folder_find =  check_folder(filepath_feature)
    continue
while is_step_folder_find == False:
    filepath_steps = input("Veuillez préciser le chemin du dossier contenant les fichiers java : ")
    is_step_folder_find = check_folder(filepath_steps)

parse_feature_file(filepath_feature)