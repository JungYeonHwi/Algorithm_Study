import math

n = int(input())

answer = []

for i in range(n) : 
    a, b = map(int, input().split())
    value = math.sqrt(a ** 2 + b ** 2) / 77
    
    answer.append([i + 1, value])
    
answer.sort(key=lambda a:(-a[1], a[0]))

for k in answer : 
    print(k[0])