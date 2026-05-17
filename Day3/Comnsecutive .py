Arr= [0,1,1,0,1,1,1,0,1,1,1,1]
count=0
for i in Arr:
    if i == 1:
        count += 1
    else:
        count=0
        
print(count)