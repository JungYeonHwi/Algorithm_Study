a = int(input())
t = int(input())
x = int(input())

bundegi = []
bun = degi = 1
n = 0

while 1 :
    prev = bun
    n += 1
    for _ in range(2) :
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(n+1) :
        bundegi.append((bun, 0))
        bun += 1
    for _ in range(n+1) :
        bundegi.append((degi, 1))
        degi += 1
    if prev < t <= bun :
        print(bundegi.index((t, x)) % a)
        break