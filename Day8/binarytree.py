class BSTNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # Insert Node
    def insertNode(rootNode, nodeValue):
        if rootNode.data is None:
            rootNode.data = nodeValue
        elif nodeValue <= rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.rightChild, nodeValue)

    # Preorder Traversal
    def preOrderTraversal(rootNode):
        if rootNode is None:
            return
        print(rootNode.data)
        BSTNode.preOrderTraversal(rootNode.leftChild)
        BSTNode.preOrderTraversal(rootNode.rightChild)
        
    #inorder traversal
    def inOrderTraversal(rootNode):
        if rootNode is None:
            return
        BSTNode.inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        BSTNode.inOrderTraversal(rootNode.rightChild)

    #postorder traversal
    def postOrderTraversal(rootNode):
        if rootNode is None:
            return
        BSTNode.postOrderTraversal(rootNode.leftChild)
        BSTNode.postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)
        
    #search Node
    def searchNode(rootnode,nodevalue):
        if rootnode.data == nodevalue:
            print("the value is found")
        elif nodevalue <rootnode.data:
            if rootnode.leftChild is None:
                print("the value is not found")
            else:
                BSTNode.searchNode(rootnode.leftChild,nodevalue)
        else:
            if rootnode.rightChild is None:
                print("the value is not found")
            else:
                BSTNode.searchNode(rootnode.rightChild,nodevalue)




# Create BST
newBST = BSTNode(None)

# Insert Nodes
BSTNode.insertNode(newBST, 70)
BSTNode.insertNode(newBST, 50)
BSTNode.insertNode(newBST, 90)
BSTNode.insertNode(newBST, 30)
BSTNode.insertNode(newBST, 60)
BSTNode.insertNode(newBST, 80)
BSTNode.insertNode(newBST, 100)
BSTNode.insertNode(newBST, 20)
BSTNode.insertNode(newBST, 40)
BSTNode.insertNode(newBST, 10)
# Traverse Tree
print("Pre-order Traversal:")
BSTNode.preOrderTraversal(newBST)

print("In-order Traversal:")
BSTNode.inOrderTraversal(newBST)

print("Post-order Traversal:")
BSTNode.postOrderTraversal(newBST)

# Search Node
print("Search for 60:")
BSTNode.searchNode(newBST, 60)