import sys
input= sys.stdin.readline

def DFS(v):
    global check
    visited[v]= True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
            visited[i] = True
            check += 1

case = 1

while 1 :
    N = int(input())
    cnt = 1
    li= dict() 
    
    if N == 0 : break
        
    graph = [ [] for _ in range(N+1)]
    manitto = []
    answer = 0
    
    for _ in range(N):
        a, b= map(str,input().split())
        manitto.append([a,b])
        
        if a not in li.keys() :
            li[a]= cnt
            cnt +=  1
        if b not in li.keys() : 
            li[b] = cnt
            cnt += 1

    for a, b in manitto: 
        k = li.get(a)
        t = li.get(b)
        graph[k].append(t)

    result = []
    for i in range(1,N+1) : 
        if i in result : 
            continue
        check = 1
        visited= [False] *(N+1) 
        DFS(i) 
        if check == visited.count(True) : 
            for i in range(len(visited)) :
                if visited[i]== True :
                    if i not in result : 
                        result.append(i)
            answer += 1 
    
    print("{} {}".format(case,answer))

    case += 1