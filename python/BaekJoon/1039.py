import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def bfs(number):
    visited = { i:set() for i in range(1,k+1)}
    length = len(number)
    q = deque([(number,0)])
    while q:
        num, cnt = q.popleft()
        if cnt == k: continue
        for i in range(length):
            for j in range(i+1,length):
                temp = num[:i] + num[j] + num[i+1:j] + num[i] + num[j+1:]
                if i == 0 and num[i] != '0' and num[j] == '0': continue
                if temp not in visited[cnt+1]:
                    visited[cnt+1].add(temp)
                    q.append((temp,cnt+1))
    if visited[k]:
        return max(map(int, visited[k]))
    return -1

n, k = map(int,input().split())
print(bfs(str(n)))
