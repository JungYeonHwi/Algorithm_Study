n, m = map(int, input().split())
k = sorted(list(set(map(int,input().split()))))
ans = []

def bt(cnt) :
    if cnt == m :
        print(*ans)
        return
    
    cnt+=1
    
    for i in k :
        ans.append(i)
        bt(cnt)
        ans.pop()
bt(0)