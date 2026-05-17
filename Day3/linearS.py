def linearSearch(array,target):
    for i in range(0,len(array)):
        if array[i] == target:
            return i
array=[1,2,3,4,5,6,8,7,9]
target=7
result=linearSearch(array,target)
if result == -1:
    print("target value not found")
else:
    print("element found at inndex:-",result)