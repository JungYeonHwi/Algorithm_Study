n = int(input())

for i in range(2, n) : 
    if n % i : 
        minN = i
        break
for j in range(n, 1, -1) : 
    if n % j : 
        maxN = j
        break

print(minN, maxN)