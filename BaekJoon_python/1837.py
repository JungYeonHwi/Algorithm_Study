P, K = map(int, input().split())

arr = [1] * K
for i in range(2, int(K**0.5)+1) :
    if arr[i] == 1 :
        for j in range(i+i, K, i):
            arr[j] = 0
prime = [i for i in range(2, K) if arr[i] == 1]

good, bad = 1, 0

for n in prime :
    if P % n == 0 :
        good, bad = 0, n
        break
    
print("GOOD" if good else f"BAD {bad}")