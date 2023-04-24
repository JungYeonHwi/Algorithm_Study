r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]
n = int(input())
 
total = []
for i in range(r - 2):
    for j in range(c - 2):
        arr = []
        for k in range(3):
            for l in range(3):
                arr.append(a[i + k][j + l])
        arr.sort()
        total.append(arr[4])
 
ans = 0
for i in total:
    if i >= n:
        ans += 1
print(ans)
