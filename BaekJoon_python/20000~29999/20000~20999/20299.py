import sys
n,k,l = map(int,sys.stdin.readline().split())
cnt = 0
tmp = []
for _ in range(n) :
    a,b,c = map(int, sys.stdin.readline().split())
    if a>=l and b>=l and c>=l :
        if a + b + c >= k : 
            cnt+=1
            tmp.append(a)
            tmp.append(b)
            tmp.append(c)
print(cnt)
print(*tmp)
