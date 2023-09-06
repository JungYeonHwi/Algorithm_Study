dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dk = [1, 0, 3, 2]


def dice_move(k) :
  if k == 0 :
    dice_visited[0][1], dice_visited[1][1], dice_visited[2][1], dice_visited[3][1] = dice_visited[3][1], dice_visited[0][1], dice_visited[1][1], dice_visited[2][1]
  elif k == 1 :
    dice_visited[0][1], dice_visited[1][1], dice_visited[2][1], dice_visited[3][1] = dice_visited[1][1], dice_visited[2][1], dice_visited[3][1], dice_visited[0][1]
  elif k == 2 :
    dice_visited[1][0], dice_visited[1][1], dice_visited[1][2], dice_visited[3][1] = dice_visited[3][1], dice_visited[1][0], dice_visited[1][1], dice_visited[1][2]
  else :
    dice_visited[1][0], dice_visited[1][1], dice_visited[1][2], dice_visited[3][1] = dice_visited[1][1], dice_visited[1][2], dice_visited[3][1], dice_visited[1][0]

def dfs(x, y) :
  cnt = 1
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < 6 and -1 < ay < 6 and map_list[ay][ax] == 1 :
      dice_move(k)
      if not dice_visited[1][1] :
        dice_visited[1][1] = True
        cnt += dfs(ax, ay)
      dice_move(dk[k])
  return cnt

for _ in range(3) :
  map_list = [list(map(int, input().split())) for _ in range(6)]
  dice_visited = [[False]*3 for _ in range(4)]
  flg = False
  for i in range(6) :
    for j in range(6) :
      if map_list[i][j] == 1 :
        dice_visited[1][1] = True
        cnt = dfs(j, i)
        flg = True
        break
    if flg : 
      break
  print('yes' if cnt == 6 else 'no')
