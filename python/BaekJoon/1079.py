import sys
input = sys.stdin.readline

def init() :
  global N, guilty_change_mat, guilty_list, T, dead
  N = int(input())
  guilty_list = list(map(int, input().split()))
  guilty_change_mat = [list(map(int, input().split())) for _ in range(N)]
  T = int(input())
  
  dead = [False]*N

def dfs(left, depth) :
  if left == 2 :
    return depth+1
  if left == 1 :
    return depth

  if left % 2 == 0 :
    result = depth+1
    
    for i in range(N) :
      if dead[i] or i == T :
        continue
      max_val, max_idx = -float('inf'), -1
      for j in range(N) :
        if dead[j] or i == j :
          continue
        guilty_list[j] += guilty_change_mat[i][j]
        if guilty_list[j] > max_val :
          max_val, max_idx = guilty_list[j], j

      if max_idx != T :
        dead[i] = True
        dead[max_idx] = True
        result = max(result, dfs(left-2, depth+1))
        dead[i] = False
        dead[max_idx] = False
        
      for j in range(N) :
        if dead[j] or i == j  :
          continue
        guilty_list[j] -= guilty_change_mat[i][j]
        
  else :
    max_val, max_idx = -float('inf'), -1
    for i in range(N) :
      if dead[i] :
        continue

      if guilty_list[i] > max_val :
        max_val, max_idx = guilty_list[i], i

    if max_idx == T :
      return depth
    else :
      dead[max_idx] = True
      result = dfs(left-1, depth)
      dead[max_idx] = False
      
  return result

def solve() :
  init()
  result = dfs(N, 0)
  print(result)

solve()
