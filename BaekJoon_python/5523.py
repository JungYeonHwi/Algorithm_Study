from sys import stdin

N = int(stdin.readline())
a = 0
b = 0

for _ in range(N) : 
    A, B = map(int, stdin.readline().split())
    
    if (A > B) : a += 1
    elif (A < B) : b += 1
    
print(a, b)