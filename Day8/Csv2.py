import csv
f = open("student.csv",'a')
a=csv.writer(f)
# a.writerow(["Stuid","Stuname","phy","Chem","Math","total","percentage","result"])
stuiid = int(input("enter student  id:"))
stuuname = input("enter student name:")
phy = int(input("enter  phy mark:"))
chem= int(input("enter chem mark:"))
math = input("enter math mark:")
total = phy+chem+math
percentage=(total/300)*100
#result pass or fail
a.writerow([stuiid,stuuname,phy,chem,math,total,percentage])
print("file has created")