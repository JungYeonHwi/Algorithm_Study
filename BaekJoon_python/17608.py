import sys

n = int(sys.stdin.readline())

stack = []
answer = 1

for _ in range(n) : 
    stack.append(int(sys.stdin.readline()))
    
m = stack[-1]

for i in range(len(stack)-1, -1, -1) : 
    if stack[i] > m : 
        answer += 1
        m = stack[i]
        
print(answer)