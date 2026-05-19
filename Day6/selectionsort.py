arr = [20,12,10,15,2]
for i in range(len(arr)):
    min = i
    j=i+1
    while j<len(arr):
        if arr[j]<arr[min]:
            min = j
        j=j+1
    arr[i],arr[min]=arr[min],arr[i]
    
print(arr)