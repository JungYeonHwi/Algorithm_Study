import sys

h, m, s = map(int, sys.stdin.readline().split())

for _ in range(int(sys.stdin.readline())) :
    arr = list(map(int, sys.stdin.readline().split()))
    if len(arr) == 1 and arr[0] == 3 : print(h, m, s)
    else : 
        t = h*3600 + m*60 + s
        t += (arr[1] if arr[0] == 1 else -arr[1])
        if t < 0 : t += 86400
        t = t % 86400
        h, m, s = t//3600, (t%3600)//60, t%60