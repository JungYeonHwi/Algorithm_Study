import sys

r, c = map(int, sys.stdin.readline().split())

graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

boolean = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == "W":
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if x <= -1 or x >= r or y <= -1 or y >= c:
                    continue
                if graph[x][y] == "S":
                    boolean = True
                    break

if boolean:
    print(0)
else:
    print(1)
    
    for i in range(r) :
        for j in range(c) :
            if graph[i][j] == '.' :
                graph[i][j] = "D"
    for k in graph :
        print(''.join(k))