## Alexis Drago

import os
import sys
import re
def find_functions_in_files(functions, directory="."):
    files_with_functions = {}
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for file_name in files:
        with open(os.path.join(directory, file_name), 'r') as file:
            file_content = file.read()
            for function in functions:
                pattern = re.compile(fr'\b{function}\b')
                if pattern.search(file_content):
                    if file_name not in files_with_functions:
                        files_with_functions[file_name] = []
                    files_with_functions[file_name].append(function)
    return files_with_functions
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_functions.py <function1> <function2> ...")
        sys.exit(1)
    functions_to_find = sys.argv[1:]
    current_directory = os.getcwd()
    files_with_functions = find_functions_in_files(functions_to_find, current_directory)
    if files_with_functions:
        print("Functions found in the following files:")
        for file, functions in files_with_functions.items():
            print(f"{file}: {', '.join(functions)}")
    else:
        print("No functions found in the files.")
