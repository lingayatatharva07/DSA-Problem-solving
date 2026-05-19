# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)

# print(factorial(4))

# def capitalizefirst(arr):
#     result=[]
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalizefirst(arr[1:])

# print(capitalizefirst(['car','taco','banana']))

# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base*power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

# def productofarray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productofarray(arr[1:])

# print(productofarray([1,2,3]))
# print(productofarray([1,2,3,10]))

# def reverse(string):
#     if len(string) <=1:
#         return string
#     return string[len(string)-1]+reverse(string[0:len(string)-1])

# print(reverse('python'))
# print(reverse('acanfoeGE'))

# def recursiverange(num):
#     if num <=0:
#         return 0 
#     return num + recursiverange(num-1)

# print(recursiverange(6))

# def ispallindrom(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return ispallindrom(strng[1:1])

# print(ispallindrom('awesome'))

# def somerecursive(arr,cb):
#     if len(arr)==0:
#         return False
#     if not(cb(arr[0])):
#         return somerecursive(arr[1:],cb)
#     return True

# def isodd(num):
#     if num%2==0:
#         return False
#     else:
#         return True
    
# print(somerecursive([1,2,3,4],isodd))
# print(somerecursive([4,6,8,9],isodd))
# print(somerecursive([4,6,8],isodd))