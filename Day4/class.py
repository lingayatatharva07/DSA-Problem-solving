# obj is a reference vairiable
# class Name:
#     age =30
#     def display(self):
#         print("Hello world")
        
# obj = Nmae()
# print(obj.age)
# obj.display()

# class Student:
#     def __init__(self): # Special attributes or function are defined by double underscore
#         self.name="prashant" #4 byte
#         self.age=30   #2byte
        
#     def display(self):
#         print("Name=",self.name)
#         print("age=",self.age)
# stuObj=Student()
# print(stuObj)

# class Message:
#     def __init__(self): #for one obj constructor will call only once
#         print("I am a constructor")
        
#     def shows(self):
#         print("class program")
# obj = Message()
# obj.shows()
# obj2 = Message()
                
#parameterize constructor
class students:
    def __init__(self,Name,age,roll_no):
        self.Name = Name
        self.age= age
        self.roll_no=roll_no
    def displaystudents(self):
         print("Name=",self.Name)
         print("age=",self.age)
         print("Roll_no=",self.roll_no)

studentObj = students("Prakash",25,101)        
studentObj.displaystudents()