string= input("enter the word:")
count=0

for i in string:
    z =ord(i)
 if z>97 and z<=122:
    continue
 elif z>=48 and z<=57:
    continue
 else:
    count +=1

print(count)