import sys
input = sys.stdin.readline

sList = list(map(str, input()))
n = int(input())

for _ in range(n) : 
    s, i, j = map(str, input().split())
    
    i = int(i)
    j = int(j)
    
    chk = ''
    for idx in range(i, j+1) :
        chk += sList[idx]
    
    print(chk.count(s))
    