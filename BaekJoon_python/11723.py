import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m) : 
    data = sys.stdin.readline().strip().split()
    
    if len(data) == 1 : 
        op = data[0]
    else : 
        op = data[0]
        n = data[1]
        num = int(n)
    
    if op == "add" : S.add(num)
    if op == "remove" : S.discard(num)
    if op == "check" : 
        if num in S : print(1)
        else : print(0)
    if op == "toggle" : 
        if num in S : S.discard(num)
        else : S.add(num)
    if op == "all" : S = set([i for i in range(1, 21)])
    if op == "empty" : S = set()
    