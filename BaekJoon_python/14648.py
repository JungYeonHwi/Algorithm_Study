n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
arr.append(0)

for _ in range(q) : 
    value = list(map(int, input().split()))
    if value[0] == 1 : 
        a, b = value[1], value[2]
        s = 0
        for i in range(a, b+1) : 
            s += arr[i]
        print(s)
        arr[a], arr[b] = arr[b], arr[a]
    if value[0] == 2 : 
        a, b = value[1], value[2]
        c, d = value[3], value[4]
        s = 0
        for i in range(a, b+1) : 
            s += arr[i]
        for i in range(c, d+1) : 
            s -= arr[i]
        print(s)