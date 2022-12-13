n = int(input())
s = 0
arr = []

for i in range(n) :
    arr.append(int(input()))  
    s += arr[i] * (-1) ** i
a = s // 2

print(a)
for i in range(n-1) :
    a = arr[i] - a
    print(a)