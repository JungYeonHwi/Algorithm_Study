import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def check(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        check(x, y, N//2)
        check(x, y+N//2, N//2)
        check(x+N//2, y, N//2)
        check(x+N//2, y+N//2, N//2)
        return
  if color == 0 : result.append(0)
  else : result.append(1)


check(0,0,N)
print(result.count(0))
print(result.count(1))