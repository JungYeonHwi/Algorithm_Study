T = int(input())
s = 0

for _ in range(T) : 
    S, A = map(int, input().split())
    
    s += A % S
    
print(s)