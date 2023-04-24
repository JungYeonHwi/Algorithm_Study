import sys
n = int(sys.stdin.readline())
c = {}
y = {}
checkx = []
checky = []
for _ in range(n):
    a,b = map(int , sys.stdin.readline().split(" "))
    checkx.append(a)
    checky.append(b)
    if a in c:
        c[a].append(b)
    else:
        c[a] = []

    if b in y:
        y[b].append(a)
    else:
        y[b] = []
checky = list(set(checky))
checkx = list(set(checkx))

ans = 0
for i in checkx:
    if c[i]:
        ans += 1
for i in checky:
    if y[i]:
        ans += 1
print(ans)