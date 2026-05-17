# string= "pranshant*is*a*good*programmer"
# new=''
# val=''
# for i in string:
#     if i!="*":
#         new+=i
#     else:
#         val+=i
# print(new)
# print(str(val+new))

input= 'aaabbbbcccceeeee'
dict={}
key=0
for i in range(len(input)):
    key=input[i]
    count=0
    for j in range(len(input)):
        
        if input[j]== key:
            count +=1
    dict[key]=count
for i,j in dict.items():    
    print(i,j,sep='',end='')
