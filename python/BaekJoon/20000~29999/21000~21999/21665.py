cnt = 0
n, m = map(int, input().split())

lst = list(range(0, m, 1))
arr1 = []

for i in range(n) : 
    arr1.append(input())
    
input()
arr2 = []

for i in range(n) : 
    arr2.append(input())
    
for x, y in zip(arr1, arr2) : 
    for i in range(m) : 
        if x[i] == y[i] : cnt += 1
        
print(cnt)