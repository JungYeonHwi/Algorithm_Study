n, k = map(int, input().split())
m = list(map(int, input().split()))

for i in range(n) :
    k -= m[i]
    if k < 0 :
        print(i+1)
        break
else :
    for i in range(n-1, -1, -1) :
        k -= m[i]
        if k < 0 :
            print(i+1)
            break