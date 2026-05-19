class Node:
    def _init_(self, data):
        self.data=data  # instance variable
        self.next=None

class LinkedList:
    def _init_(self):
        self.head=None

linkedlist = LinkedList()

linkedlist.head=Node(5)
second         =Node(10)
third          =Node(15)
fourth         =Node(20)

#connecting nodes
linkedlist.head.next=second
second.next=third
third.next=fourth 
fourth.next=None

# display Linked List
while linkedlist.head != None:
    print(linkedlist.head.data  , " ")
    linkedlist.head=linkedlist.head.next