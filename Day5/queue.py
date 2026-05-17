#Queue Ds
# 1.EnQueue
# 2.DeQueue
# 3.Display queue
# 4.isfull
# 5.isempty
# 6.peek

import sys 
class Queue:
    def __init__(self ,size):
        self.myQueue = [] #creating stack
        self.Quesize = size
    
    def isfull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return False
            
    def Enqueue(self,value):
        if self.isfull():
            print("Queue is full")
        else:
            self.myQueue.append(value)
            print("element EnQueued")
        
  
    
    def isempty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        
    
    def Dequeue(self):
         if self.isempty():
             print("Queue is empty")
         else:
            print(self.myQueue.pop(0))
            print("element pop")
            
            
    def peek(self): #peek will just return the top  most element
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.myQueue[-1])
            
    def delQueue(self):
        self.mystack = None
    def display(self):
        for i in range((len(self.myQueue)-1),-1,-1):
             print("|_",self.myQueue[i],"_|")

size =  int(input("enter the size of the stack"))
obj = Queue(size)
print("Stack has created:")
while True:
    print("1.  Enqueue Operation")
    print("2. Display queue")
    print("3. Dequeue")
    print("4. peek") 
    print("5. Delete Queue:")
    print("6.Exit")
    choice =  int(input("Enter the choice:"))
    if choice == 1:
        value = int(input("Enter value to push in Queue:"))
        obj.Enqueue(value)
    elif choice ==2:
        obj.display()
    elif choice == 3:
        obj.Dequeue()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.delQueue()
    elif choice==6:
        sys.exit()
    