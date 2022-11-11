n = int(input())

stack = [i for i in range(1, n+1)]
discard = []

while len(stack) != 1 : 
    discard.append(stack.pop(0))
    stack.append(stack.pop(0))

for i in discard :
    print(i, end = ' ')
    
print(stack[0])