import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


def DFS(start, group) :
    global error

    if error : return

    visited[start] = group  

    for i in graph[start]:
        if not visited[i]:
            DFS(i, -group) 
        elif visited[start] == visited[i] : 
            error = True 
            return  


T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)] 
    visited = [False] * (V + 1) 
    error = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1) :
        if not visited[i] : 
            DFS(i, 1)
            if error :  
                break

    if error : print('NO')
    else : print('YES')