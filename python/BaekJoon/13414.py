import sys

K, L = map(int, sys.stdin.readline().split())

dt = dict()

for i in range(L) :
    cn = sys.stdin.readline().rstrip()
    dt[cn] = i

dt = sorted(dt.items(), key=(lambda x: x[1]))

cnt = 0

for i in dt :
    if cnt == K :
        break
    
    print(i[0])
    cnt += 1