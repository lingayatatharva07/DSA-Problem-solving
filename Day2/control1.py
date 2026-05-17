# s="Python are High level programming language"
# print(s.lower())
# print(s.upper())
# print(s.title())    
# print(s.capitalize())
# print(s.swapcase())

#formatting example
# name="prashant"
# sal=5000
# age=28
# print(" {} salary is {}  age is {}".format(name,sal,age))
# print(" {0} salary is {1}  age is {2}".format(name,sal,age))
# print("{X} salary is {Y}  age is {Z}".format(X=name,Y=sal,Z=age))
# A=1
# print(f"{A} is a good boy")

# name="prashant"
# for i in name: #i=0:p r a s h a n t
#     print(i) 

 #write a program to remove duplicate character from the string
# name="prashant"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname += i
         
# print(newname)

#above string in reverse order
# name="prashant"
# new=""
# n = len(name)
# for i in range (n-1,-1,-1):
#       new += name[i]
# print(new)

#check the palindrom
# name="Help4code"
# new=""
# n = len(name)

# for i in range(n-1,-1,-1):
#     new += name[i]
    

# if name== new :
#     print("palindrom")
# else:
#    print("not in palindrom")

#Vowel and Constraint 
# string= input("enter the word:")
# vowels=['a','e','i','o','u']
# cons=0
# vow=0
# for i in string:
#     if i in vowels:
#         vow += 1
#     else:
#         cons += 1

# print(vow)
# print(cons)
        
  #anagram
# name1= "listen"
# name2="silent"
# ana= False
# for i in name1:
#     if i in name2:
#         ana = True
        
# if ana :
#     print("in anagram")
# else:
#     print("not anagram")        
   
#Bodmass
a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)
        