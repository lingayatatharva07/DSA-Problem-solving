import sys 
class stack:
    def __init__(self):
        self.mystack = [] #creating stack
        
    def push(self,value):
        self.mystack.append(value)
        print("element push")
    
    def isempty(self):
        if self.mystack == []:
            return True
        else:
            return False
    
    def pop(self):
         if self.isempty():
             print("Stack is empty")
         else:
            print(self.mystack.pop())
            print("element pop")
    def peek(self): #peek will just return the top  most element
        if self.isempty():
            print("stack is empty")
        else:
            print(self.mystack[-1])
    def delstack(self):
        self.mystack = None
    def display(self):
        for i in range((len(self.mystack)-1),-1,-1):
             print("|_",self.mystack[i],"_|")

obj = stack()
print("Stack has created:")
while True:
    print("1. Push Operation")
    print("2. Display Stack")
    print("3. pop")
    print("4. peek") 
    print("5. Delete")
    print("7.Exit")
    choice =  int(input("Enter the choice:"))
    if choice == 1:
        value = int(input("Enter value to push in stack:"))
        obj.push(value)
    elif choice ==2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.delstack()
    elif choice==7:
        sys.exit()
    
    