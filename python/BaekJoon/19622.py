import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(node, t) :
    t += arr[node][2]
    if arr[node][1] > maxValue :
        res.append(t)        
    for n in range(node+1, N) :
        if arr[node][1] > arr[n][0] :
            continue
        DFS(n, t)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[0], x[1]))
res = []
maxValue = max([s for s, e, n in arr])
for i in range(N):
    DFS(i, 0)
print(max(res))