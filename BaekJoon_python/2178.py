def DFS_ITERATION(graph, root) :
      visited = [] 
      stack = [root]

      while(stack) : 
          node = stack.pop()
          
          if(node not in visited) :
              visited.append(node)
              stack.extend(graph[node])
      return visited

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n) :
    graph.append(list(map(int, input())))
    
    