s = "hello world"
stk = []
result = ""

for ch in s:
    if ch != " ":
        stk.append(ch)
    else:
        while stk:
            result += stk.pop()
        result += " "

while stk:
    result += stk.pop()

print(result)