#! python3

import sys
import uuid 
from graphviz import Digraph
import readDataCSV

nb_node=0
extract=[]
dot = Digraph(comment='Mon graph orienté')

# finallement, ce que j'ai fait c'est un arbre (et pas un graph orienté, car on peut avoir plusieurs parent dans ce 
# deuxieme cas alors qu'ici il n'y a qu'un unique parent) 
class MyNode:
    def hasParent(self):
        if self.parent:
            return True
        else:
            return False

    def getName(self):
        return self.name
    
    def getInfo(self):
        print("ce node aura : ", self.maxChild, "efnants")
        print(f"il a actuellement {len(self.list_child)} enfants")
    
    def createAllChild(self, lvl=0):
        # print("creation lvl : ", lvl)
        # for i in range(lvl+1):
        #     print("***", end="")
        if self.maxChild <0:
            return False
        for i in range(self.maxChild):
            self.list_child.append(MyNode(max_child=self.maxChild, hello='enfant niveau :'+str(lvl), parent=self))
            if lvl > 0:
                self.list_child[len(self.list_child)-1].createAllChild(lvl=lvl-1)
            #print("======")
        self.has_created_child = True
        return True
    
    def addOneChild(self, dataStr, dataVal):
        self.list_child.append(MyNode(max_child=self.maxChild, val=dataVal, hello='enfant ', parent=self, nodeData=dataStr))
        self.has_created_child = True

    def initFromDataOnlyLevelOne(self, dataList=[]):
        # uid;pseudo;data;level;parent
        for line in dataList:
            print("Processing data : ", line)
            data = line.split(';')
            self.list_child.append(MyNode(max_child=self.maxChild, 
                                          val=42, hello='enfant ', 
                                          parent=self, 
                                          nodeData=data[2], 
                                          uuidForced=data[0], 
                                          pseudo=data[1]))
        self.has_created_child = True

    
    def displayAllChild(self, lvl=0):
        if self.has_created_child == False:
            return False
        print("->", self.id)
        for i in self.list_child:
            if lvl > 0:
                i.displayAllChild(lvl=lvl+1)
            print("|", end='')
            for j in range(lvl):
                print(" ", end='')
            print('>', i.id) 
            global nb_node
            nb_node = nb_node + 1

    def displayGraph(self, lvl=0, and_data=False):
        for i in range(lvl):
            print(" ", end='')
        if and_data:
            print("|-", lvl, "->", self.id, " data : ", self.node_data)
        else:
            print("|=", lvl, "->", self.id)

        for i in self.list_child:
            i.displayGraph(lvl=lvl+1, and_data=and_data)

    def displayMyChild(self):
        if self.has_created_child == False:
            return False
        for i in self.list_child:
            print(f"id:{i.id} data : {i.node_data}")
        return True
    

    def __init__(self, max_child=3, val=42, hello="le noeud", parent=None, nodeData="", uuidForced=None, pseudo=""):
        if uuidForced is not None:
            self.id = uuidForced
        else:
            self.id = uuid.uuid4()
        self.data = []
        self.maxChild = max_child
        self.val = val
        self.node_data = nodeData
        self.name = pseudo if pseudo else 'le nom du node'
        self.parent = parent
        self.has_created_child=False
        self.list_child = []
        #parent=None
        # if parent != None:
        #     print("mon parent est : ", parent.id)
        # print("bonjour : ", hello, "mon id : ", self.id)

def genDataForPicture(main_node, lvl=0, and_data=False):
    global extract
    for i in main_node.list_child:
        if and_data == False:
            extract.append( (str(main_node.id)[30:], str(i.id)[30:]) )
        else :
            #ceci peut ne pas fonctionner car la donnée n'est pas nécessairement unique
            extract.append( (main_node.node_data, i.node_data) )
        if i.has_created_child:
            genDataForPicture(i, lvl=lvl+1, and_data=and_data)

def genPicture(fileName="mon_arbre_oriente"):
    global extract
    print(extract)
    unic_extract = list(set(extract))

    for src, dst in unic_extract:
        dot.edge(src, dst)
    
    dot.render(fileName, format="png", cleanup=True)

def readFile(nameFile):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()

    for i in input:
        print(i)

# dataToInject : (UNIQUEMENT les niveaux 1) liste des données à injecter dans l'arbre 
def dynamicGen(dataToInject=[]):
    master_node = MyNode(hello='debut de /', max_child=-1, nodeData='/')
    tst = master_node
    fisrtInit = False

    cmdList = ['init', 'doc', 'add', 'display', 'display_child', 'info', 'moovein', 'reset_cursor', 'goto_parent', 'picture', 'quit']
    cmdDict = {'init' : '\t\tInitialise les enfants du nœud courant (WIP)',
               'doc' : '\t\tAffiche la documentation des commandes', 
               'add' : '\t\tAjoute un enfant au nœud courant', 
               'display' : '\tAffiche le graphe', 
               'display_child' : 'Affiche le(s) enfant(s) du nœud courant', 
               'info' : '\t\tAffiche les informations du nœud courant', 
               'moovein' : '\tSe déplace dans un enfant du nœud courant', 
               'reset_cursor' : '\tRetourne au nœud maître', 
               'goto_parent' : '\tSe déplace vers le parent du nœud courant', 
               'picture' : '\tGénère une image du graphe (via Digraph)', 
               'quit' : '\t\tQuitte le programme'
               }

    if dataToInject:
        master_node.initFromDataOnlyLevelOne(dataToInject)
    
    while True:
        entry = input("Que voulez-faire?\n--$>")

        if entry == 'quit':
            print("Au revoir")
            return True
        elif entry == 'doc':
            for cmd in cmdList:
                print(f"{cmd} : {cmdDict[cmd]}")
        elif entry == 'init' and not fisrtInit:
            tst.createAllChild(lvl=0)
            fisrtInit = True
            print("Initialisation des enfants terminée")
        elif entry == 'init' and fisrtInit:
            print("Les enfants ont déjà été initialisés")
        elif entry == 'add':
            entry_bis = input("Que voulez-ajouter?\n--$>")
            tst.addOneChild(dataStr=entry_bis, dataVal=42)
        elif entry == 'display':
            tst.displayGraph(and_data=True)
        elif entry == 'display_child':
            rtr = tst.displayMyChild()
            print('retour : ', rtr)
        elif entry == 'info':
            rtr = tst.getInfo()
        elif entry == 'moovein':
            print("dans quel enfant se deplacer ? ")
            tst.displayMyChild()
            entry_bis = input("choississez\n--$>")
            try:
                entry_int = int(entry_bis)
                if entry_int < 0:
                    print("le nœud choisit ne peut etre negatif")
                elif entry_int > len(tst.list_child):
                    print("le nœud choisit ne peut dépasser le tableau")
                else:
                    tst = tst.list_child[entry_int]
            except:
                print(" une erreur est survenu : avez vous choisit une bonne valeur ?")
        elif entry == 'reset_cursor':
            print("retour au nœud maitre")
            tst = master_node
        elif entry == "goto_parent":
            if tst.hasParent():
                tst = tst.parent
            else : 
                print(" on n'a pas de parent ")
        elif entry == "picture":
            global extract
            extract = []
            genDataForPicture(main_node=master_node, and_data=True)
            fileName = "toto_dyn_tree"
            genPicture(fileName=fileName)

def main(av):
    print("Bonjour - nothing special here ^^")
    if len(av) >= 2:
        if av[1] == "dyn":
            dynamicGen()
            return 0
        #readFile(av)
        if av[1] == "read":
            fileLst = readDataCSV.readCSV(av[2])
            fileLst = readDataCSV.orderByLevel(fileLst)
            onlyFirstLevel = readDataCSV.getOnlyLevelOne(fileLst)
            for line in onlyFirstLevel:
                print(line)
            return 0
        if av[1] == "readndyn":
            fileLst = readDataCSV.readCSV(av[2])
            fileLst = readDataCSV.orderByLevel(fileLst)
            onlyFirstLevel = readDataCSV.getOnlyLevelOne(fileLst)
            for line in onlyFirstLevel:
                print(line)
            dynamicGen(dataToInject=onlyFirstLevel)
            return 0
    else:
        print("on ne fait rien")

    tst = MyNode(hello='debut', max_child=20)
    #print(tst)

    level_child=0

    print(tst.getName())
    print("ID node principal = ", tst.id)
    print(tst.has_created_child)
    print("has Parettn : ", tst.hasParent())
    tst.createAllChild(lvl=level_child)
    print("has created child", tst.has_created_child)

    print('---les enfants du principal---')
    tst.displayMyChild()
    
    print('--tout le graph.. en fait l\'abre--')
    #tst.displayAllChild(lvl=level_child)
    tst.displayGraph()
    print("totla node = ", nb_node)
    #print(tst.getInfo())

    print("--fin--")
    genDataForPicture(tst)
    genPicture()

if __name__ == '__main__':
    main(sys.argv)