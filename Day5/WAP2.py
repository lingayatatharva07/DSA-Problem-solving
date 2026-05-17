#write a program to accept student name and marks  from the keyboard and creates a dictionary  also display student marks by taking student name
# student = {}
# n = int(input("Enter the number of students:"))
# for i in range(n):
#     name = input("Enter student name:")
#     marks = float(input("Enter student marks:"))
#     student[name] = marks
# print("Student Dictionary:", student)
# search_name = input("Enter student name to display marks:")
# if search_name in student:
#     print("Marks of", search_name, ":", student[search_name])
# else:
#     print("Student not found.")


# n = int(input("Enter the number of students:"))
# d={}
# for i in range(n):
#     name = input("enter the name of student")
#     marks= input("enter the marks")
#     d[name] = marks
# while True:
#     name=input("enter the student  name to get marks")
#     marks=d.get(name,-1)
#     if marks == -1:
#         print("Student Not Found")
#     else:
#         print("the marks of",name,"are",marks)
#         option=input("do you want tofind another  students marks[YES|NO]")
#         if option == "No":
#             break
# print("thanks for using our Application")

#write a program to acess each character of string in forward and backward direction by using while loop
# input = "Learning Python is very easy"
# i = 0
# print("Characters in forward direction:")
# while i < len(input):
#     print(input[i], end=" ")
#     i += 1
# print("\nCharacters in backward direction:")
# i = len(input) - 1
# while i >= 0:
#     print(input[i], end=" ")
#     i -= 1

# str1= input("enter the string ")
# s=0
# for i  in str1 :
#     if i in str1 == " ":
#         str1[i]==str1
        
# print(i)
     
# v = ['a','e','i','o','u']
# w= input("Enter the word where we will search the vowels:") 
# found = []
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('found vowels=',found)
# print('Unique vowels',len(found),'from the given word=',w)       

# x,y,z = map(int,input().split())
# mylist=[]
# for i in range(x):
#     a=int(input())
#     mylist.append(a)
# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end=' ')

# import datetime

# date = datetime.datetime.now()
# print("it is now:{:%d/%m/%y %H:%M:%S}".format(date))

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)

#list comprehension 
# val=[2**i for i in range(1,6)]
# print(val)
# val=[i*i for i in range(1,11)]
# print(val)
#Dictionary comprehension 
# val={x:x*x for x in range(1,6)}
# print(val)
# val={x:2*x for x in range(1,6)}
# print(val)

# a,b=[int(x) for x in input("Enter 2 number:").split()]
# print("Product is :", a*b)
# a,b,c=[float(x) for x in input("Enter 3 number:").split()]
# print("Product is :", a+b+c)

# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("this is not in myy budget")
#         continue
#     print(item)
# else:
#     print("you have purchased everything")

# username = "admin"
# password=  "admin"
# while True:
#     u = input("enter the user name")
#     p= input("enter the password")
#     if u == username and p == password:
#         print("login successfully")
#         break
#     else:
#         print("invalid")
import time
class Tower:
    def __init__(self):
        print("welcome to tower of hanoi")
        print()
        print("Given problem A[3,2,1]  B=[]   C=[]   ")
        print()
        print("Expected Output A=[]    B=[]    C=[]")
        self.A=[]
        self.B=[]
        self.C=[]
        
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("items in tower A\n")
        
    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "   ",   "B=", self.B  , "   ","C=",self.C)
        print("Pass one complete====================================")
        
    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "   ",   "B=", self.B  , "   ","C=",self.C)
        print("Pass two complete====================================")
        
    def pass3(self):
        self.temp = self.A.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "   ",   "B=", self.B  , "   ","C=",self.C)
        print("Pass three complete====================================")
    
    def pass4(self):
        self.temp = self.C.pop(2)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "   ",   "B=", self.B  , "   ","C=",self.C)
        print("Pass four complete====================================")
     
    def pass5(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "   ",   "B=", self.B  , "   ","C=",self.C)
        print("Pass five complete====================================")
        
    def pass6(self):
        self.temp = self.B.pop(1)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "   ",   "B=", self.B  , "   ","C=",self.C)
        print("Pass six complete====================================")
               
    def pass7(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "   ",   "B=", self.B  , "   ","C=",self.C)
        print("Pass seven complete====================================")
        
Obj= Tower()
Obj.tower(3)
Obj.tower(2)
Obj.tower(1)
Obj.pass1()
Obj.pass2()
Obj.pass3()
Obj.pass4()
Obj.pass5()
Obj.pass6()
Obj.pass7()
                  

