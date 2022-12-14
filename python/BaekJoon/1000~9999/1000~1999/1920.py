import sys 

n = int(sys.stdin.readline())
nList = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))

for i in mList : 
    if i in nList : print(1)
    else : print(0)