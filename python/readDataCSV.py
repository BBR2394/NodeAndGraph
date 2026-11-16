#! python3

import sys

def orderByLevel(lst):
    lst.pop(0)  # remove header if present
    # <:-c  (O_O)!
    return sorted(lst, key=lambda x: int(x.split(';')[3]))

# attention erreur : cette fonction suppose que la liste n'a plus son header
def getOnlyLevelOne(lst):
    # \(”˚☐˚)/ l'autocomplétion!..........
    return [line for line in lst if int(line.split(';')[3]) == 1]

def readCSV(fileName):
    lst = []
    with open(fileName, 'r') as fd:
        input = fd.read()
        lst = input.splitlines()
    return lst

def main(av):
    print("Lecture du fichier de csv")
    if len(av) >= 2:
        fileName = av[1]
        content = readCSV(fileName)
        content = orderByLevel(content) 
        for line in content:
            print("level", line.split(';')[3], end=' ')
            print(line)
        print("\nOnly level one:")
        level_one = getOnlyLevelOne(content)
        for line in level_one:
            print("level", line.split(';')[3], end=' ')
            print(line)

    else:
        print("Aucun fichier spécifié")

if __name__ == '__main__':
    main(sys.argv)