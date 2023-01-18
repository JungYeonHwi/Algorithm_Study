import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
toping = [0]*n

for i in range(n) :
    toping[i] = int(input())
    
toping.sort(reverse=True)
total = c
cnt = 0
res = total//a

while 1:
    for j in range(n) :
        total += toping[j]
    cnt += 1
    now = total//(a+(b*cnt))
    if res <= now : res = now
    else : 
        print(res)
        exit()