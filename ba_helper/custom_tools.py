import os, glob
import termcolor, tqdm

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

def classify_and_step(current_index, input_list, current_step, given_list, when_list, then_list):
    """Classify in the right state (aka: Given, When, Then) all And steps.
    It takes a list. This list is shortened with the current_index.
    Then its searching for the first Given/When/Then word to append the current_step in the right list.

    Args:
        current_index (int): index of the current step
        input_list (list): list to process 
        current_step (str): step to add
        given_list (str): list where you want to store your given
        when_list (str): list where you want to store your when
        then_list (str): list where you want to store your then
    """
    for i in range(current_index, 0, -1):
        if "Given" in input_list[i-1]:
            if current_step not in given_list:
                given_list.append(current_step)
                break
        elif "When" in input_list[i-1]:
            if current_step not in when_list:
                when_list.append(current_step)
                break
        elif "Then" in input_list[i-1]:
            if current_step not in then_list:
                then_list.append(current_step)
                break
        else:
            continue

def parse_feature_file(feature_folder, given_list, when_list, then_list):
    """This function reads all feature files then it puts in different list all steps.
    It also checks if the current step not already in the list
    
    Args:
        feature_folder (str): the path to the folder that contains feature files
        given_list (str): list where you want to store your given
        when_list (str): list where you want to store your when
        then_list (str): list where you want to store your then
    """
    feature_list = []

    for root, dirs, files in os.walk(feature_folder):
        for current_file in files:
            if current_file.endswith(".feature"):
                feature_list.append(os.path.join(root, current_file))

    for feature_file in feature_list:
        with open(feature_file, "r") as open_file:
            current_feature = open_file.readlines()
        processed_lines = [x.replace("\n", "") for x in current_feature if any([x.startswith(i) for i in ["Given", "When", "Then", "And"]])]
        #my dumber way to do that was if x.startswith("Given") or x.startswith("When") or x.startswith("Then") or x.startswith("And")
        
        pbar = tqdm.tqdm(processed_lines)
        for line in pbar:
            pbar.set_description("Récupération des steps")
            if line.startswith("Given"):
                line = line.replace("Given ", "")
                if line not in given_list:
                    given_list.append(line)
            elif line.startswith("When"):
                line = line.replace("When ", "")
                if line not in when_list:
                    when_list.append(line)
            elif line.startswith("Then"):
                line = line.replace("Then ", "")
                if line not in then_list:
                    then_list.append(line)
            elif line.startswith("And"):
                line_without_and = line.replace("And ", "")
                classify_and_step(processed_lines.index(line), processed_lines, line_without_and, given_list, when_list, then_list)

def write_in_file(step_folder, given_list, when_list, then_list):
    """This function creates a java file. Then it processes all element in given/when/then lists and write correct steps in the java file
    
    Args:
        step_folder (str): the path to the folder that contains step files
        given_list (str): list where you want to store your given
        when_list (str): list where you want to store your when
        then_list (str): list where you want to store your then
    """
    path_to_java = os.path.join(step_folder, "java_file_from_script.java")
    f = open(path_to_java, "w")
    
    pbar_given = tqdm.tqdm(given_list)
    for given_line in pbar_given:
        pbar_given.set_description("Ecriture des given")
        step_name = given_line.replace("\"", "\\\"")
        function_name = given_line.replace(" ", "_").replace("\"", "").replace("\'","").replace(":", "")
        given_to_write = f"@Given(\"^{step_name}$\")\npublic void {function_name}(){{\n}}\n\n"
        f.write(given_to_write)

    pbar_when = tqdm.tqdm(when_list)
    for when_line in pbar_when:
        pbar_when.set_description("Ecriture des when")
        step_name = when_line.replace("\"", "\\\"")
        function_name = when_line.replace(" ", "_").replace("\"", "").replace("\'","").replace(":", "")
        when_to_write = f"@When(\"^{step_name}$\")\npublic void {function_name}(){{\n}}\n\n"
        f.write(when_to_write)

    pbar_then = tqdm.tqdm(then_list)
    for then_line in pbar_then:
        step_name = then_line.replace("\"", "\\\"")
        pbar_then.set_description("Ecriture des then")
        function_name = then_line.replace(" ", "_").replace("\"", "").replace("\'","").replace(":", "")
        then_to_write = f"@Then(\"^{step_name}$\")\npublic void {function_name}(){{\n}}\n\n"
        f.write(then_to_write)
    f.close()