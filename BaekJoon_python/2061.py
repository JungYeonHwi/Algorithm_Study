L, K = map(int, input().split())

arr = [1] * K
for i in range(2, int(K**0.5)+1) :
    if arr[i] == 1 :
        for j in range(i+i, K, i):
            arr[j] = 0
prime = [i for i in range(2, K) if arr[i] == 1]

good = 1

for n in arr :
    if L%n == 0 :
        print(f"BAD {n}")
        good = 0
        break
    
if good == 1 : print("GOOD")