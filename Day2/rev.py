# num = 123456
# a = num%10
# num = num //10
# b = num%10
# num = num //10
# c= num%10
# num = num //10
# d=num%10
# num = num //10
# e=num%10
# f=num//10
# rev = a*100000+b*10000+c*1000+d*100+e*10+f*1
# print(rev)
#-------------------------------------------------------------------------

Amount = int(input("Please Enter Amount for Withdraw: "))
print("100 notes = ", Amount // 100)
print("50 notes = ", (Amount % 100) // 50)
print("20 notes = ", ((Amount % 100) % 50) // 20)
print("10 notes = ", (((Amount % 100) % 50) % 20) // 10)
print("5 notes = ", ((((Amount % 100) % 50) % 20) % 10) // 5)
print("2 notes = ", ((((Amount % 100) % 50) % 20) % 10 % 5) // 2)
print("1 notes = ", ((((Amount % 100) % 50) % 20) % 10 % 5) % 2 //1)