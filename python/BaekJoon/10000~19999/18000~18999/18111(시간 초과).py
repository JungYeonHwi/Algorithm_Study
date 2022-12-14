import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
idx = 0

for target in range(257):
    maxTarget, minTarget = 0, 0

    for i in range(n) :
        for j in range(m) :

            if graph[i][j] >= target :
                maxTarget += graph[i][j] - target

            else :
                minTarget += target - graph[i][j]
                
    if maxTarget + b >= minTarget :
        # 시간 초를 구하고 최저 시간과 비교 
        if minTarget + (maxTarget * 2) <= answer :
            answer = minTarget + (maxTarget * 2)
            idx = target

print(answer, idx)