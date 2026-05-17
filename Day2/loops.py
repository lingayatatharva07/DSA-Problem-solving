# for i in range(1,4):
#  for j in range(1,4):
#    print(i,end=" ")
#  print()
   
# n = int(input("enter the numberof rows"))
# for i in range(1,n+1):
#     for j in range (1,1+n):
#         print(chr(64+i),end=" ")
#     print()
# output:
#     enter the numberof rows5
# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E 

# n = int(input("enter the numberof rows"))
# for i in range(1,n+1):
#     for j in range (1,1+i):
#         print(chr(64+i),end=" ")
#     print()

# A 
# B B 
# C C C 
# D D D D 
# E E E E E

# n = int(input("enter the numberof rows"))
# for i in range(1,n+1):
#     for j in range (1,n+2-i):
#         print(chr(64+i),end=" ")
#     print()
# A A A A A 
# B B B B 
# C C C 
# D D 
# E 

# import time
# n = int(input("enter the numberof rows"))
# for i in range(1,n+1):
#     print(" "*(n-1),end=" ")
#     for j in range (1,i+1):
#         time.sleep(3)
#         print("*",end=" ")
#     print()

s=[1,2,3,4]
new=[]
for i in s:
    product=1
    for j in s:
        if j==i:
            continue
        else:
            product *=j
    new.append(product)        
            
print(new)
                        