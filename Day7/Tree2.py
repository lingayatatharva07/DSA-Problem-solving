class tree:
    def __init__(self,data):
        self.data= data
        self.child = []
    
    def __str__(self,level =0):
        ret = " "*level +str(self.data)+"\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret
    
    
    def addchild(self,object):
        self.child.append(object)
        print("Node added")
    
        
rootnode = tree("N1")
N2  = tree("N2")
N3  = tree("N3")
N4 = tree("N4")
N5 = tree("N5")
N6 = tree("N6")
N7 = tree("N7")
N8 = tree("N8")

rootnode.addchild(N2)
rootnode.addchild(N3)
N2.addchild(N4)
N2.addchild(N5)
N3.addchild(N6)
N4.addchild(N7)
N4.addchild(N8)

print(rootnode)