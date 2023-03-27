import math

x, n = map(int, input().split())
arr = [x]

for i in range(n) : 
    if arr[-1] % 2 == 0 : 
        value = math.floor(arr[-1] / 2) ^ 6
        arr.append(value)
    else : 
        value = (2 * arr[-1]) ^ 6
        arr.append(value)
    
print(arr[-1])