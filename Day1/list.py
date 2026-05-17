# mylist = ["prashant","ashish","komal","ankush",60,50,"prashant"]
# print(mylist)
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:6:2])

# mylist[2]="akashya"
# print(mylist)

# if "ankush" in mylist:
#     print("yes ankush is present in the list")

# mylist.append("harsh")
# mylist.append("laxman")
# print(mylist)

# mylist.insert(2,"harsh")
# print(mylist)

# newlist = mylist.copy()
# print(newlist)


# newlist = [["prashant", "ashish"], ["komal", "ankush"], [60, 50]]
# print("example of multidimensional list")
# print(newlist)
# print(newlist[0][0])
# print(newlist[0][1])
# print(newlist[1][0])
# print(newlist[1][1])
# print(newlist[2][0])
# print(newlist[2][1])

# list2=[50,25.50,'prashant']
# del list2[0]
# print(list2)

# list2=[50,25.50,'prashant']
# list2.clear()
# print(list2)

# name='prashant'
# print(name)
# myname=list(name)
# print(myname)

#sorting example
# mylist=[50,25.50,10,5,100]
# mylist.sort()
# print(mylist)

#allising example
# mylist=[50,25.50,10,5,100]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[50,25.50,10,5,100]
# for i in mylist:
#     print(i)


# list1=[0,1,4,0,2,5]
# for i in list1:
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)

# list1=[7,3,9,2,8]
# list1.sort()
# print(list1[-2])

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# arr=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# fruit_list1 = ["Apple","Berry","Cherry","Papaya"]
# fruit_list2= fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = "Guava"
# fruit_list3[1] = "Kiwi"

# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == "Guava":
#         sum += 1
#         if ls[1] == "Kiwi":
#             sum += 20
#     print(sum)

# A= [1,2,3]
# B= [2,3,4]          
# C= [3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)

mylist = []
n = int(input("enter the number of elements in the list: "))
for i in range(n):
    element = int(input("enter the element: "))
    mylist.append(element)
print(mylist)

for i in range(len(mylist)-1):
    for j in range(i+1, len(mylist)):
        if mylist[i] > mylist[j]:
            mylist[i], mylist[j] = mylist[j], mylist[i]