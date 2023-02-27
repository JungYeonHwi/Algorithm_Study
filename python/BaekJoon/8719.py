import sys

input = sys.stdin.readline

for _ in range(int(input())) : 
    a, b = map(int, input().split())
    
    n = 0
    
    while a <= b : 
        a = a ** 2
        n += 1
        
    print(n)