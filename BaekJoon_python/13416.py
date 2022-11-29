import sys
for _ in range(int(sys.stdin.readline())) :
    m = 0
    for i in range(int(sys.stdin.readline())) :

        arr = list(map(int,sys.stdin.readline().split()))
        if max(arr) >= 0 : m += max(arr)
    print(m)