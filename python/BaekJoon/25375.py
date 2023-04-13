import sys
input=lambda:sys.stdin.readline().strip('\n')

for t in range(int(input())) :
    g, s = map(int,input().split())
    print(int(s % g == 0 and s > g))