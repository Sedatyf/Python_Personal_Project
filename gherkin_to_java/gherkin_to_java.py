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
def check_folder(path):
    """Check if the inputted folder exists.

    Args:
        path (string): the path for the folder to be scan

    Returns:
        boolean: True if folder is found
    """
    if os.path.exists(path):
        termcolor.cprint("Dossier trouvé !", "green")
        return True
    else:
        termcolor.cprint("Dossier non trouvé !", "red")
        return False

def classify_and_step(current_index, input_list, current_step):
    """Classify in the right state (aka: Given, When, Then) all And steps.
    It takes a list. This list is shortened with the current_index.
    Then its searching for the first Given/When/Then word to append the current_step in the right list.

    Args:
        current_index (int): index of the current step
        input_list (list): list to process 
        current_step (str): step to add
    """
    shortened_list = input_list[:current_index+1]
    for i in range(current_index, 0, -1):
        if "Given" in input_list[i-1]:
            if current_step not in given:
                given.append(current_step)
                break
        elif "When" in input_list[i-1]:
            if current_step not in when:
                when.append(current_step)
                break
        elif "Then" in input_list[i-1]:
            if current_step not in then:
                then.append(current_step)
                break
        else:
            continue

def parse_feature_file(feature_folder):
    """This function reads all feature files then it puts in different list all steps.
    It also checks if the current step not already in the list
    
    Args:
        feature_folder (str): the path to the folder that contains feature files
    """
    for feature_file in glob.glob(os.path.join(feature_folder, "*.feature")):
        with open(feature_file, "r") as open_file:
            current_feature = open_file.readlines()
        processed_lines = [x.replace("\n", "") for x in current_feature if x.startswith("Given") or x.startswith("When") or x.startswith("Then") or x.startswith("And")]
        
        for line in processed_lines:
            if line.startswith("Given"):
                line = line.replace("Given ", "")
                if line not in given:
                    given.append(line)
            elif line.startswith("When"):
                line = line.replace("When ", "")
                if line not in when:
                    when.append(line)
            elif line.startswith("Then"):
                line = line.replace("Then ", "")
                if line not in then:
                    then.append(line)
            elif line.startswith("And"):
                line_without_and = line.replace("And ", "")
                classify_and_step(processed_lines.index(line), processed_lines, line_without_and)

def write_in_file(step_folder):
     """This function creates a java file. Then it processes all element in given/when/then lists and write correct steps in the java file
    
    Args:
        step_folder (str): the path to the folder that contains step files
    """
    path_to_java = os.path.join(step_folder, "java_file_from_script.java")
    f = open(path_to_java, "w")
    
    for given_line in given:
        step_name = given_line.replace("\"", "\\\"")
        function_name = given_line.replace(" ", "_").replace("\"", "").replace("\'","").replace(":", "")
        given_to_write = f"@Given(\"^{step_name}$\")\npublic void {function_name}(){{\n}}\n\n"
        f.write(given_to_write)
    for when_line in when:
        step_name = when_line.replace("\"", "\\\"")
        function_name = when_line.replace(" ", "_").replace("\"", "").replace("\'","").replace(":", "")
        when_to_write = f"@When(\"^{step_name}$\")\npublic void {function_name}(){{\n}}\n\n"
        f.write(when_to_write)
    for then_line in then:
        step_name = then_line.replace("\"", "\\\"")
        function_name = then_line.replace(" ", "_").replace("\"", "").replace("\'","").replace(":", "")
        then_to_write = f"@Then(\"^{step_name}$\")\npublic void {function_name}(){{\n}}\n\n"
        f.write(then_to_write)
    f.close()

#Script
while is_feature_folder_find == False:
    filepath_feature = input("Veuillez préciser le chemin du dossier contenant les fichiers .features : ")
    is_feature_folder_find =  check_folder(filepath_feature)
while is_step_folder_find == False:
    filepath_steps = input("Veuillez préciser le chemin du dossier contenant les fichiers java : ")
    is_step_folder_find = check_folder(filepath_steps)

parse_feature_file(filepath_feature)
write_in_file(filepath_steps)
termcolor.cprint("Tous les tests ont été traités !", "green")
