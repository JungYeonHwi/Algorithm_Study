a, b = map(int, input().split())
n = int(input())

for _ in range(n) : 
    value = int(input())
    
    if value > 1000 : 
        diff = value - 1000
        re = value - diff
    else : 
        diff = 0
        re = value
    
    print(value, re * a + diff * b)