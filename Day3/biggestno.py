def findbiggestno(samplearray):
    biggestno=samplearray[0]  #=================================> O(1)
    for index in range(1,len(samplearray)): #===================> O(n)
        if samplearray[index]>biggestno:  #=================================> O(1)
            biggestno=samplearray[index] #=================================> O(1)
    print(biggestno)#=================================> O(1)
    
samplearray = [5,7,9,2,3,4]#=================================> O(1)
findbiggestno(samplearray)#=================================> O(1)


#total time complexity
# O(1)+O(1)+O(1)+O(1)+O(1)+O(N) = O(N)