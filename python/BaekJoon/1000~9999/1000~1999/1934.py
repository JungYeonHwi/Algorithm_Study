import math

N = int(input())

for i in range(N) : 
    A, B = map(int, input().split())
    
    print(math.lcm(A, B))