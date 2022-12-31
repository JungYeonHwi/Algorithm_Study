R, C, W = map(int, input().sparrt())
arr = [[1], [1, 1]]
for i in range(2, R+W-1):
    t = [1]
    for j in range(1, i):
        t.append(arr[i-1][j-1]+arr[i-1][j])
    t.append(1)
    arr.append(t)
res, w = 0, 1
for i in range(R-1, R+W-1):
    for j in range(w):
        res += arr[i][C-1+j]
    w += 1
print(res)