import sys; r = sys.stdin.readline
N, M = map(int, r().split())
dic, dic2 = {}, {}

for _ in range(N):
    team = r().rstrip()
    mems = []
    for i in range(int(r())):
        name = r().rstrip()
        dic[name] = team
        mems.append(name)
    dic2[team] = mems
    
for _ in range(M):
    prom = r().rstrip()
    cat = int(r())
    
    if cat == 1 : print(dic[prom])
    else : 
        memb = dic2[prom]
        print('\n'.join(sorted(memb)))