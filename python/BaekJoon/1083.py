n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
    maxx = arr[i]
    val = 0
    if s == 0 : break
    for j in range(i+1, n) :
        x = j-i
        if arr[j] > maxx :
            maxx = arr[j]
            val = x
        if x >= s:
            break
    if val :
        s -= val
        arr.remove(maxx)
        arr.insert(i, maxx)

for x in arr:
    print(x, end=' ')