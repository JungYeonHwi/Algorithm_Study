n, s = input().split()
n = int(n)
s = str(s)

tmp = []

for _ in range(n) : 
    a, b = input().split()
    if a == s : ans = b
    tmp.append((a,b))
    
cnt = 0
for i in range(len(tmp)) :
    if tmp[i][1] == ans :
        if tmp[i][0] != s : cnt += 1
    if tmp[i][0] == s : 
        print(cnt)
        break