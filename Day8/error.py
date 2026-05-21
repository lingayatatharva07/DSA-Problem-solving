# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer value: ")
# except:
#     print("ABC")

import logging
logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
try:
    a = int(input("enter first integer no"))
    b = int(input("enter second integer no"))
    print(a/b)
except (ZeroDivisionError,ValueError) as message:
     print(message)
     logging.exception(message)
print("Logging level is set up. Check 'newfile.txt for log details.")