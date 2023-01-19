import sys

N, M = map(int, sys.stdin.readline().split())
rule = []
yeon = []
a = 0

for i in range(N) : 
    b, c = list(map(int, sys.stdin.readline().split()))
    a += b
    rule.append([a,c])
    
a = 0

for i in range(M) :
    b, c = list(map(int, sys.stdin.readline().split()))
    a += b
    yeon.append([a,c])

diffRule = [0] * 100
diffYeon = [0] * 100

for i in range(100) :
    for j in range(len(rule)) :
        if i < rule[-j-1][0] : diffRule[i] = rule[-j-1][1]
    for j in range(len(yeon)) : 
        if i < yeon[-j-1][0] : diffYeon[i] = yeon[-j-1][1]

max = 0

for i in range(100) :
    if max < diffYeon[i] - diffRule[i] : max = diffYeon[i] - diffRule[i]
print(max)