import os
import sys
import re

def check_functions(file_path, functions):
    with open(file_path, 'r') as file:
        content = file.read()
        found_functions = re.findall(r'\b(?:' + '|'.join(functions) + r')\b', content)
        if len(found_functions) != len(functions):
            forbidden_functions = set(found_functions) - set(functions)
            print(f"ERREUR: Fonction(s) interdite(s) trouvee(s) dans {file_path}: {', '.join(forbidden_functions)}")
            return False
        else:
            print(f"Tout est bon dans {file_path}")
            return True

def main():
    if len(sys.argv) < 2:
        print("Utilisation: python3 analyseur.py fonction1 fonction2 ...")
        sys.exit(1)

    functions = sys.argv[1:]

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        if file.endswith('.c'):
            if not check_functions(file, functions):
                sys.exit(1)

if __name__ == "__main__":
    main()
