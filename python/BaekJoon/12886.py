from collections import deque

# 너비 우선 탐색 함수
def bfs():
    global a, b, c, total, visited
    q = deque()
    # 두 그룹 큐에 넣기
    q.append((a, b))
    # 방문 표시
    visited[a][b] = True
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 총 돌의 개수는 항상 일정하므로 남은 그룹 돌 개수 계산 가능
        z = total - x - y
        if x == y == z:
            print(1)
            return
        # 두 그룹끼리 돌의 개수 비교
        for a, b in (x, y), (y, z), (x, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            # 돌의 개수가 같은 그룹은 건너뛰기
            else:
                continue
            # 두 그룹이 돌을 분배한 후 남은 그룹의 돌 개수
            c = total - a - b
            # 가장 작은 값을 x, 가장 큰 값을 y로 받기
            x = min(a, b, c)
            y = max(a, b, c)
            # 중복 제거
            # 해당 돌의 개수만큼 아직 분배되지 않았다면
            if not visited[x][y]:
                # 분배 실시
                q.append((x, y))
                # 방문 표시
                visited[x][y] = True
    print(0)


# 돌의 정보 입력받기
a, b, c = map(int, input().split())
# 전체 돌의 개수
total = a + b + c
# 방문 표시
visited = [[False] * (total + 1) for _ in range(total + 1)]

# 총 돌의 개수가 3의 배수가 아니라면
if total % 3 != 0:
    # 같은 개수로 만들 수 없으므로 0 출력
    print(0)
# 3의 배수라면
else:
    # bfs 함수 실행
    bfs()
