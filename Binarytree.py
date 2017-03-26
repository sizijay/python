class Node:
    def __init__(self,val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self.add(val, self.root)
    def _add(self, val, node):
        if(val<node.v):
            if(node.l !=None):
                self._(val, node.l)
            else:
                node.l=Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r=Node(val)
    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)
    def _printTree(self, node):
        if(node !=None):
            self._printTree(node.l)
            print (str(node.v) + ' ')
            self._printTree(node.r)
    
    

tree=Tree()
tree.add(50)
tree.add(10)
tree.add(15)
tree.add(8)
tree.printTree()

