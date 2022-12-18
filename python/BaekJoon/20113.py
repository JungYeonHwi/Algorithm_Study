n = int(input())
vote = list(map(int, input().split(" ")))

cnt = [0 for x in range(n)]

for i in vote : 
    if i == 0 : continue
    else : cnt[i-1] += 1
    
m = max(cnt)

if cnt.count(m) >= 2 or m == 0 : print("skipped")
else : print(cnt.index(m) + 1)
