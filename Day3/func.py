#function is a block of code which executs every time we want
# def hello():
#     print("hello world")
    
    
# hello()

# def arithmetic():
#     a=int(input("enter the number:"))
#     b=int(input("enter the number:"))
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div

# print(arithmetic())

# def arithmetic(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# result=arithmetic(5,5)
# print("arithmetic=",result)
#-------------------------------------------------
#keyword argument
# keyword name must be same as argument name

# def credential(username,password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("invalid credentials")
        
# credential(username="admin",password="admin" )

#----------------------------------------------------
#default Argument
def cityName(city="pune"):
    print(city)
    
# cityName("Nagpur")
# cityName("mumbai")
# cityName() #here no value is passed so the default value will be print

#varaiable length argument / varariable number argument
# #use  * as am perfix to print all the values
# def cityname(*name):
#     print(name)
    
# cityname("Nagpur","delhi","Pune","mumbai")

#----------------------------------------------------
#Modularity approach in function
#sys is the library of function which calls exit function
import sys
def add():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    print(a+b)

def sub():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    print(a-b)
    
def mul():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    print(a*b)
    
def div():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    print(a/b)
    
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sys.exit()