import math

n = int(input())
arr = list(map(int, input().split()))
answer = []

for i in range(1, len(arr)) : 
    a = arr[0]
    b = arr[i]
    
    value = math.gcd(a, b)
    
    qnsah = a // value
    qnswk = b // value
    
    result = str(qnsah) + "/" + str(qnswk)
    
    answer.append(result)
    
for i in answer : 
    print(i)