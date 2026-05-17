#WAP to count the frequency of elements in a list and print the elements with their frequency. using dictionary
s=[1,2,2,3,4,3,5]
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for key,value in dict.items():
    print(key,":",value)    