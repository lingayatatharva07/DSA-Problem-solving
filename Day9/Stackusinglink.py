#Stack using Linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode  #yield is used to return value
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head ==None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        node.next =self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.LinkedList.head.value
        
    def delete(self):
        self.LinkedList.head = None

customStack = Stack()

print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)

print("Top element is:", customStack.peek())
print("Popped element:", customStack.pop())
print("Popped element:", customStack.pop())
print("Top element is:", customStack.peek())

customStack.delete()
print(customStack)
print(customStack.isEmpty())
print(customStack.pop())