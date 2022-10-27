a, b = map(int, input().split())

arr = []

for _ in range(a) : 
    n = int(input())
    arr.append(n)
    
s = sum(arr)
value = b // s

for i in arr : 
    print(i * value)