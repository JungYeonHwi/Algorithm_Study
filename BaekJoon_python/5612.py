n = int(input()); m = int(input())
value = 0

for _ in range(n) :
    a, b = map(int, input().split())
    m = m + a - b
    if m < 0 : 
        value = 0
        break
    if value < m : value = m
print(value)