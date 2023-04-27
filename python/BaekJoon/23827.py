n = int(input())
nl = list(map(int,input().split()))
sl = sum(nl)
res = 0
for i in nl :
    sl -= i
    res = (res + i * sl) % 1000000007
print(res)