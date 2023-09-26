dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, T = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]
xi = list()
di = list()
ki = list()
for _ in range(T):
    tx, td, tk = map(int, input().split())
    xi.append(tx)
    di.append(td)
    ki.append(tk)
    
for i in range(T):
    # 원판 배수
    cur_x = xi[i]
    # 방향 0: 시계, 1: 반시계
    cur_d = di[i]
    # 회전 칸수
    cur_k = ki[i]
    
    # 1. 배수 원판 회전시키기.
    # 시계 방향으로 회전
    if cur_d == 0:
        # idx가 0부터 시작하므로 cur_x - 1부터 시작한다고 표현
        for j in range(cur_x - 1, N, cur_x):
            # cur_k만큼 시계방향으로 회전
            for _ in range(cur_k):
                temp = numbers[j].pop()
                numbers[j].insert(0, temp)
    
    # 반시계 방향으로 회전
    elif cur_d == 1:
        # idx가 0부터 시작하므로 cur_x - 1부터 시작한다고 표현
        for j in range(cur_x - 1, N, cur_x):
            # cur_k만큼 반시계방향으로 회전
            for _ in range(cur_k):
                temp = numbers[j].pop(0)
                numbers[j].append(temp)

    # 2. 원판에 수가 남아있으면, 인접하면서 수가 같은 것을 모두 찾는다.
    temp_num = 0
    for num in numbers:
        temp_num += sum(num)
    # 원판에 수가 없으면 break
    if temp_num == 0:
        break
    
    # 인접하면서 수가 같은 것을 모두 찾는다.
    visited = [[0] * (M) for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if numbers[r][c] == 0 or visited[r][c] == 1:
                continue
            queue = [(r, c)]
            while queue:
                kr, kc = queue.pop()
                
                for k in range(4):
                    current_r = kr + dr[k]
                    current_c = kc + dc[k]
                    # 열끼리 연산
                    if current_c < 0:
                        current_c = M - 1
                    elif current_c > M - 1:
                        current_c = 0
                    if 0 <= current_r and current_r < N and visited[current_r][current_c] == 0:
                        # 인접한 것끼리 숫자가 같을 경우
                        if numbers[kr][kc] == numbers[current_r][current_c]:
                            # 방문 처리
                            visited[kr][kc] = 1
                            visited[current_r][current_c] = 1
                            queue.append((current_r, current_c))
    # visited한 것이 있으면 == 인접한 것이 있으면 0으로 만듦.
    check = 0
    for rr in range(N):
        for cc in range(M):
            if visited[rr][cc] == 1:
                numbers[rr][cc] = 0
                check = 1
    # 인접한 수가 없다면 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
    if check == 0:
        avg = 0
        cnt = 0
        # 평균 계산
        for rr in range(N):
            for cc in range(M):
                if numbers[rr][cc] != 0:
                    avg += numbers[rr][cc]
                    cnt += 1
        # 평균과 비교   
        avg /= cnt
        for rr in range(N):
            for cc in range(M):
                if numbers[rr][cc] != 0:
                    # 평균보다 크면 1 빼줌
                    if numbers[rr][cc] > avg:
                        numbers[rr][cc] -= 1
                    # 평균보다 작으면 1 더해줌
                    elif numbers[rr][cc] < avg:
                        numbers[rr][cc] += 1

ans = 0
for idx in range(N):
    ans += sum(numbers[idx])
print(ans)
