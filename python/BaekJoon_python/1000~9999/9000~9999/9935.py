s = input()
v = input()

lastChar = v[-1]
stack = []
length = len(v)

for char in s :
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == v :
        del stack[-length:]

answer = ''.join(stack)

if answer == '' : print("FRULA")
else : print(answer)