string = input("enter the sentence:")
countW=0
for i in string:
    if i == " ":
        countW += 1
    elif string == "":
        countW=0

print(countW)