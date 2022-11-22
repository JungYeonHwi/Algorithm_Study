while 1 :
    arr = list(map(int, input().split()))
    if arr[0] == -1 : break
    l = len(arr)
    cnt = 0
    for i in range(l - 1) :
        if arr[i] * 2 in arr:
            cnt += 1
    print(cnt)