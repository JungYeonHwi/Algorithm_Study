n = int(input())
aSum = 0
bSum = 0

for i in range(n) : 
    a, b = map(int, input().split())
    
    if a > b : aSum += (a + b)
    elif a < b : bSum += (a + b)
    else : 
        aSum += a
        bSum += b

print(aSum, bSum)