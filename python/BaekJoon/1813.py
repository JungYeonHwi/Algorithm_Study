import sys
n = int(sys.stdin.readline())
hs = list(map(int, sys.stdin.readline().split()))
tmp = [0] * 100001
cnt = 0
checker = 0
for i  in range(n) :
    tmp[hs[i]] += 1
for i in range(len(tmp)) :
    if tmp[i] == i : 
        cnt = i
        checker = 1
if checker == 0 : 
    print(-1)
    exit()
else : print(cnt)