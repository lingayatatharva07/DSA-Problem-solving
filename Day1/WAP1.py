#wap to accept there paper marks and calculate the percentage and check if she/he is passed in all the subject , so print pass else print fail.
math= int(input("Enter marks of math: "))
chem= int(input("Enter marks of chemistry: "))
phy= int(input("Enter marks of physics: "))
total= math+chem+phy
per= total/3
print("Percentage: ",per)
if math>=35 and chem>=35 and phy>=35:
    print("Pass")
else:    print("Fail")
gender= input("Enter gender: ")
if per >=65 and gender=="male":
    print("Eligible for placement")   
else :
    print("Not eligible for placement")       