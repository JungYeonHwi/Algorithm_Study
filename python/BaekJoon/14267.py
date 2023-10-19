import sys
from collections import defaultdict
def dfs(a):
	visit = [False]*(n+1)
	queue = []
	queue.append(a)
	while queue:
		next = queue.pop()
		if visit[next]:
			continue
		visit[next] = True
		
		for i in tree[next]:
			if not visit[i]:
				queue.append(i)
				total[i] += total[next]  # 직속 상사의 칭찬 수치 더해줌


n,m = map(int,input().split())
n_list = list(map(int,input().split()))
total = [0]*(n+1)
tree = defaultdict(list)
for i in range(1,n):
	tree[n_list[i]].append(i+1)

for i in range(m):
	a,b = map(int,sys.stdin.readline().split())
	total[a]+=b
dfs(1)
print(*total[1:])
