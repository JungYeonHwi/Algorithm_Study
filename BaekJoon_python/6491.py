import sys

nums = list(map(int, sys.stdin.read().split()))

for n in nums :
    if n == 0 : break
    arr = []
    for i in range(1, n) :
        if n % i == 0 :
            if i not in arr : arr.append(i)
            if n//i not in arr and n//i != n : arr.append(n//i)
            
    if sum(arr) == n : print(f"{n} PERFECT")
    elif sum(arr) < n : print(f"{n} DEFICIENT")
    else : print(f"{n} ABUNDANT")