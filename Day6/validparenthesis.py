s="({([()])})"
stack = []
matching = {')': '(', '}': '{', ']': '['}

for char in s:
    if char in matching:             
        top = stack.pop() if stack else '#'
        if matching[char] != top:
            print(False)
    else:                             
        stack.append(char)
        
print(len(stack) == 0)
            