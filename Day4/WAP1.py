# #count the repeated no. in the integer
# num = [5,7,8,3,7,8,9,2,3]
# new=[]
# for i in range(len(num)):
#     count=0
#     key=num[i]
#     j=i+1
#     while j<len(num):
#         if key == num[j]:
#             new.append(key)
#         j=j+1
# print(len(new))    


num = [5,7,8,3,7,8,9,2,3]
count=0
for i in range(len(num)):
    key = num[i]
    j = i+1
    for j in range(j<len(num)):
        if key == num[j]:
            count =j+1
print(count)
