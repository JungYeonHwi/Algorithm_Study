n,l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
arr = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i].append(graph[j][i])

arr = graph + arr
cnt = 0
flag = False
for path in arr:
    visit = [0]*n
    for k in range(1, n):
        if path[k-1] == path[k]:
            continue
        elif path[k-1] - path[k] == 1:
            if sum(path[k:k+l]) == path[k]*l and sum(visit[k:k+l]) == 0:
                visit[k:k+l] = [1]*l
            else:
                flag = True
                break
        elif path[k] - path[k-1] == 1:
            if sum(path[k-l:k]) == path[k-1]*l and sum(visit[k-l:k]) == 0:
                visit[k-l:k] = [1]*l
            else:
                flag = True
                break
        else:
            flag = True
            break
    if flag:
        flag = False
    else:
        cnt += 1
print(cnt)
