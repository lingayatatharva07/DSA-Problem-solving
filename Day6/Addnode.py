class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addNodeatBeg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  
            self.tail = new_node

    def addNodeatEnd(self, data):
        self.addNode(data)  

    def addNodeinBetween(self, data):
        pos = int(input("Enter position after which to insert: "))
        temp = self.head
        count = 1
        while temp is not None and count < pos:
            temp = temp.next
            count += 1
        if temp is None:
            print("Position not found")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            if temp == self.tail:  
                self.tail = new_node

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

if __name__ == '__main__':
    ll = LinkedList()
    while True:
        print('\n1. Add Node Linkedlist :')
        print('2. Add Node in Beginning :')
        print('3. Add Node in Between :')
        print('4. Add Node in End  :')
        print('5. Display Linked List :')
        print('6. Exit')
        ch = int(input('Enter your choice :'))
        if ch == 1:
            value = int(input('Enter value for node:'))
            ll.addNode(value)
            print('Node added successfully.')
        elif ch == 2:
            value = int(input('Enter value for node:'))
            ll.addNodeatBeg(value)
            print('Node added successfully.')
        elif ch == 3:
            value = int(input('Enter value for node:'))
            ll.addNodeinBetween(value)
            print('Node added successfully.')
        elif ch == 4:
            value = int(input('Enter value for node:'))
            ll.addNodeatEnd(value)
            print('Node added successfully.')
        elif ch == 5:
            ll.display()
        elif ch == 6:
            break
        else:
            print('Invalid choice')