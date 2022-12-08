from collections import deque

n = int(input()) # 총 컴퓨터의 수
m = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[]*n for _ in range(n+1)] # 간선을 입력받을 경로

for _ in range(m) : # 간선을 입력 받을 경로
    a, b = map(int,input().split()) # 연결되어 있는 컴퓨터 번호 쌍 입력
    graph[a].append(b) # 번호 쌍 추가
    graph[b].append(a) # 번호 쌍 추가

cnt = 0 # 정답 변수
visited = [0]*(n+1) # 방문한 것을 확인하기 위한 변수

def BFS(n) : # BFS 함수
    global cnt # 정답 변수
    visited[n] = 1 # 방문한 것을 저장
    queue = deque([n]) # 1번 컴퓨터와 연결된 것을 확인
    
    while queue : # queue가 다 도는 동안
        v = queue.popleft() # 왼쪽 값을 pop
        for i in graph[v] : # 연결된 것들 중에서 확인
            if not visited[i] : # 방문하지 않은 것을 확인
                queue.append(i) # queue에 저장
                visited[i] = True  # 방문한 것을 저장
                cnt += 1 # 정답 증가
                print(i)
                
BFS(1) # 1번 컴퓨터가 연결된 것을 확인
print(cnt) # 정답 출력