from collections import deque

stk = deque()
time = deque()
answer = deque()

n = int(input())

for i in range(n) :
    x = list(map(int,input().split()))
    
    if x[0] == 1 :
        stk.append(x[1])
        time.append(x[2])
    else :
        pass 
    if time :
        time[-1] -= 1 
        if time[-1] == 0 :
            time.pop()
            answer.append(stk.pop())
            
print(sum(answer))