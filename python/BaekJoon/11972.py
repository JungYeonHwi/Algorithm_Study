n, m, d, s = map(int,input().split())
person = [[] for i in range(n)]
countlist = [0 for _ in range(m+1)]

for i in range(d) :
    p, m, t = map(int,input().split())
    person[p-1].append((m,t))
for i in range(s) :
    p, t = map(int,input().split())
    for history in person[p-1] :
        if history[1] < t :
            countlist[history[0]] += 1
ans = 0
for i in range(len(countlist)) :
    if countlist[i] < s :
        continue
    tmp = 0
    for per in person :
        for history in per :
            if history[0] == i :
                tmp += 1
                break
            
    ans = max(ans, tmp)
print(ans)