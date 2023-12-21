from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_list = [[i] + list(map(int, input().split())) for i in range(1, M+1)]
if N <= 2 or M <= N-3:
  print(-1)
  exit()

edge_dict = defaultdict(list)
visited = [False]*(N+1)
for i, a, b in edge_list :
  edge_dict[a].append((i, b))
  edge_dict[b].append((i, a))

def dfs(node) :
  visited[node] = True
  node_list = [node]
  edge_list = []
  q = [node]
  while q :
    node = q.pop()
    for idx, nxt in edge_dict[node] :
      if not visited[nxt] :
        visited[nxt] = True
        edge_list.append(idx)
        node_list.append(nxt)
        q.append(nxt)

  return edge_list, node_list, node

edges, nodes, last_nodes = list(), list(), list()
for i in range(1, N+1) :
  if not visited[i] :
    _edges, _nodes, _last_node = dfs(i)
    edges.append(_edges)
    nodes.append(_nodes)
    last_nodes.append(_last_node)

if len(nodes) > 2 :
  print(-1)
  exit()
if len(nodes) == 2 :
  if len(nodes[0]) == len(nodes[1]) :
    print(-1)
    exit()
  print(len(nodes[0]), len(nodes[1]))
  for i in range(2) :
    print(*nodes[i])
    print(*edges[i])
  exit()

edges, nodes, last_node = edges[0], nodes[0], last_nodes[0]
cur_edges = list()
for idx in edges :
  _, a, b = edge_list[idx-1]
  if a == last_node or b == last_node:
    continue
  cur_edges.append(idx)

print(len(nodes)-1, 1)
print(*[n for n in nodes if n != last_node])
print(*cur_edges)
print(last_node)
print()
