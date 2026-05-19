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
    
        
rootnode = tree("Drinks")
Hot  = tree("Hot")
Cold  = tree("Cold")
Tea = tree("Tea")
Coffee = tree("Coffee")
NonAlcohalic = tree("NonAlcohalic")
Alcohalic = tree("Alcohalic")

rootnode.addchild(Hot)
rootnode.addchild(Cold)
Hot.addchild(Tea)
Hot.addchild(Coffee)
Cold.addchild(NonAlcohalic)
Cold.addchild(Alcohalic)

print(rootnode)