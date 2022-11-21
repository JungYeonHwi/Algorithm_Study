import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int,input().split())
guitars = set()
for _ in range(N):
    name, pos = input().split()
    value = ''
    for chr in pos :
        if chr=="Y" :
            value += '1'
        else : 
            value += '0'
    guitars.add(int(value, 2))
    
guitars -= {0}
if not guitars :
    print(-1)
    exit()
m = 0

for i in range(1,N+1) :
    for combs in combinations(guitars,i):
        total = 0
        for num in combs : total |=num
        
        cnt = 0
        for j in range(M) :
            if total&(1<<j) : cnt+=1
        if m < cnt:
            m = cnt
            abswer = i

print(abswer)