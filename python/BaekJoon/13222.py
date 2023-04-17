import math

n, a, b = map(int, input().split())

value = math.sqrt(a ** 2 + b ** 2)

for _ in range(n) : 
    nn = int(input())
    
    if value >= nn : print("YES")
    else : print("NO")