import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    if x < 0 or x >= h or y < 0 or y >= w : return False

    if graph[x][y] == 1 :

        graph[x][y] = 0

        DFS(x-1, y)
        DFS(x-1, y-1)
        DFS(x, y-1)
        DFS(x+1, y-1)
        
        DFS(x+1, y)
        DFS(x+1, y+1)
        DFS(x, y+1)
        DFS(x-1, y+1)
        return True
    return False

while 1 :
    w,h = map(int,input().split())

    if w == 0 and h ==0 : break
    else : 
        graph = []
        for _ in range(h) :
            graph.append(list(map(int, input().split())))

        result = 0
        for i in range(h) :
            for j in range(w) :
                if DFS(i, j) == True :
                    result += 1
        print(result)