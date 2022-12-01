n, k = map(int, input().split())
arr = []

for i in range(1, k+1) : 
    value = n * i
    num = str(value)[::-1]
    arr.append(int(num))
    
print(max(arr))