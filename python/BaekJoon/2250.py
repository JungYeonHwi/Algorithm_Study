import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[-1, -1, -1] for x in range(n+1)]
for i in range(n):
    node, lc, rc = map(int, sys.stdin.readline().split())
    tree[node][1] = lc
    tree[node][2] = rc
    tree[lc][0] = n
    tree[rc][0] = n
root = -1
for i in range(1, n+1):
    if tree[i][0] == -1:
        root = i

visit = [[-1, -1] for x in range(n+1)] # r: level, c: dist
def bfs(root):
    maxdepth = 0
    queue = deque([root])
    visit[root][0] = 0
    while queue:
        node = queue.popleft()
        lc = tree[node][1]
        rc = tree[node][2]
        if lc != -1:
            if visit[lc][0] == -1:
                visit[lc][0] = visit[node][0] + 1
                maxdepth = max(visit[lc][0], maxdepth)
                queue.append(lc)
        if rc!= -1:
            if visit[rc][0] == -1:
                visit[rc][0] = visit[node][0] + 1
                maxdepth = max(visit[rc][0], maxdepth)
                queue.append(rc)
    return maxdepth

global dist
dist = 0
def inorder_search(node):
    global dist
    if tree[node][1] != -1:
        inorder_search(tree[node][1])
    dist += 1
    visit[node][1] = dist

    if tree[node][2] != -1:
        inorder_search(tree[node][2])

maxdepth = bfs(root)
inorder_search(root)
maxdist = 0
minlevel = 1e10

if n == 1:
    print(1)
    print(1)

else:
    for d in range(maxdepth+1):
        minval = 1e10
        maxval = 0
        for i in range(1, n + 1):
            if d == visit[i][0]:
                minval = min(visit[i][1], minval)
                maxval = max(visit[i][1], maxval)
        if maxdist < maxval-minval+1:
            minlevel = d+1
            maxdist = maxval-minval+1

    print(minlevel)
    print(maxdist)
