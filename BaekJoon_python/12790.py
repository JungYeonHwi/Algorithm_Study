for _ in range(int(input())):
    arr = list(map(int, input().split()))
    s = [arr[i] + arr[i+4] for i in range(4)]
    answer = max(s[0], 1) + max(s[1], 1) * 5 + max(s[2], 0) * 2  + s[3] * 2
    print(answer)