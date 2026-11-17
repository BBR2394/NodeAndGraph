#! python3

import sys
import pandas as pds
from enum import Enum


def orderByLevel(lst):
    lst.pop(0)  # remove header if present
    # <:-c  (O_O)!
    return sorted(lst, key=lambda x: int(x.split(';')[3]))

# attention erreur : cette fonction suppose que la liste n'a plus son header
def getOnlyLevelOne(lst):
    # \(”˚☐˚)/ l'autocomplétion!..........
    return [line for line in lst if int(line.split(';')[3]) == 1]

class Method(Enum):
    MANUAL = 1
    PANDAS = 2

class MyDataFromCSV:
    def __init__(self):
        self.df = None
        self.list = None
        self.selected_method = None
        

def readCSV(fileName, method):
    lst = []
    MyDat = MyDataFromCSV()
    
    if method == Method.MANUAL:
        MyDat.selected_method = Method.MANUAL
        with open(fileName, 'r') as fd:
            input = fd.read()
            lst = input.splitlines()
        MyDat.list = lst
    elif method == Method.PANDAS:
        MyDat.selected_method = Method.PANDAS
        df = pds.read_csv(fileName, sep=';')
        MyDat.df = df
        #lst = df.astype(str).agg(';'.join, axis=1).tolist()

    return MyDat

def main(av):
    print("Lecture du fichier de csv")

    which_method = Method.PANDAS
    MyDat = None
    
    if len(av) >= 2:
        fileName = av[1]
        if which_method == Method.MANUAL:
            MyDat = readCSV(fileName, Method.MANUAL)
            content = MyDat.list
            content = orderByLevel(content) 
            for line in content:
                print("level", line.split(';')[3], end=' ')
                print(line)
            print("\nOnly level one:")
            level_one = getOnlyLevelOne(content)
            for line in level_one:
                print("level", line.split(';')[3], end=' ')
                print(line)
        elif which_method == Method.PANDAS:
            MyDat = readCSV(fileName, Method.PANDAS)
            content = MyDat.df
            print(content)

    else:
        print("Aucun fichier spécifié")

if __name__ == '__main__':
    main(sys.argv)