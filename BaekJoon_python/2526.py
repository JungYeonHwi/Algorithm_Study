n, p = map(int, input().split())
arr = []
arr.append(n)

x = n

while 1 : 
    x = x * n % p

    if x not in arr : arr.append(x)
    else : break

idx = 0

for i in range(len(arr)) : 
    if x == arr[i] : 
        idx = i
        break

print(len(arr) - idx)