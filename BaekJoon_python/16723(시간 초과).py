import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for idx in range(1, n+1) : 
    n = idx * 2
    value = 0
    
    i = 0
    
    while 1 : 
        tmp = 2**i
        if tmp > n : break
        else : 
            if n % tmp == 0 : 
                value = tmp
        
        i += 1
    
    answer += value
    
print(answer)