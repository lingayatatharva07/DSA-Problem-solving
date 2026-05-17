#Row wise max value
#100,198,333,323
#122,232,221,111
#223,565,245,764

list=[[100,198,333,323],
      [122,232,221,111],
      [223,565,245,764]]
newlist=[]
for i in range(3):
    j=0
    max = list[i][j]
    for j in range(4):
        c_max=list[i][j]
        if max < c_max:
            max=c_max
    newlist.append(max)
print(newlist)