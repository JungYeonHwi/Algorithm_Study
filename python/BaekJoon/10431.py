for _ in range(int(input())):
    a = list(map(int, input().split()))
    case, arr = a[0], a[1:]
    answer = 0
    for i in range(1, 20):
        m, idx = max(arr)+1, i
        for j in range(i):
            if arr[j] > arr[i] and arr[j] < m:
                m = arr[j]
                idx = j
        if idx != i:
            arr = arr[:idx] + [arr[i]] + arr[idx:i] + arr[i+1:]
            answer += i-idx
    print(case, answer)