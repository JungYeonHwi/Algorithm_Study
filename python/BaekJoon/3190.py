from collections import deque

n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 2

l = int(input())
times = {}
for _ in range(l):
    a, b = input().split()
    times[int(a)] = b

def turn(char):
    global current_dir
    if char == 'L':
        current_dir = (current_dir - 1) % 4
    else:
        current_dir = (current_dir + 1) % 4

# east, south, west, north
dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()
q.append((0,0))
x, y = 0, 0
arr[x][y] = 1
time, current_dir = 0, 0

while 1:
    time += 1
    x, y = x + dx[current_dir], y + dy[current_dir]

    if x < 0 or y < 0 or x >= n or y >= n:
        break

 
    if arr[x][y] == 2:
        arr[x][y] = 1
        q.append((x,y))
        if time in times:
            turn(times[time])
    
    elif arr[x][y] == 0:
        arr[x][y] = 1
        q.append((x,y))
        tx, ty = q.popleft()
        arr[tx][ty] = 0
        if time in times:
            turn(times[time])
    
    else:
        break

print(time)
