n = int(input())
A = [[] for _ in range(n)]
visited = [False]*n
P = [0]*n # 가격의 상대 비율
lcm = 1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0] #i는 (b,p,q)형태로 저장되어 있음
        if not visited[next]:
            P[next] = P[v]*i[2]//i[1] #v번째 상대가격을 이용한 next의 상대 가격
            DFS(next)
for i in range(n-1):
    a, b, p, q = map(int, input().split())
    A[a].append((b,p,q)) #a가 p가격일 때 b는 q 가격
    A[b].append((a,q,p)) #b가 q가격일 때 a는 p 가격
    lcm *= ((p*q)//gcd(p,q))

P[0] = lcm
DFS(0)
mgcd = P[0] # 모든 수의 최대 공약수를 mgcd라 하자.(multi gcd)

for i in range(1,n):
    mgcd = gcd(mgcd,P[i])
    
for i in range(n):
    print(int(P[i]//mgcd), end=' ')
