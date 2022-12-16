import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    initial = list(map(str, sys.stdin.readline().rstrip("\n")))
    target = list(map(str, sys.stdin.readline().rstrip("\n")))
    cnt = []

    for i in range(n) :
        if initial[i] != target[i] : cnt.append(initial[i])

    if not cnt : print(0)
    elif cnt.count("B") >= cnt.count("W") : print(cnt.count("B"))
    else : print(cnt.count("W"))