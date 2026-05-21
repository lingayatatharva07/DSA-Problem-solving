import csv
f = open("employee.csv",'a')
a=csv.writer(f)
# a.writerow(["empID","empname","emp age"])
empid = int(input("enter employee empid:"))
empname = input("enter employee name:")
age = int(input("enter employee age:"))
a.writerow([empid,empname,age])
print("file has created")