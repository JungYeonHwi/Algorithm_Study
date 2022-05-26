n, m = map(int, input().split()) # n, m 입력 받기
data = [] # 기존 보드판 저장 변수
result = [] # 개수를 확인할 변수

for _ in range(n) : # 행마다 반복
    data.append(input()) # 보드판 저장

for i in range(0, n-7) : # 8 × 8로 잘라서 확인
    for j in range(0, m-7) : # 8 × 8로 잘라서 확인 
        count1 = 0 # 변수 초기화
        count2 = 0 # 변수 초기화
        for x in range(i, i+8) : # 8 × 8 범위를 B와 W로 번갈아가면서 검사
            for y in range(j, j+8) : # 8 × 8 범위를 B와 W로 번갈아가면서 검사
                if (x+y) % 2 == 0 : # 인덱스 합이 짝수인 칸인지 검사
                    if data[x][y] != 'W' : count1 += 1 # 0,0 값이 B인 경우
                    if data[x][y] != 'B' : count2 += 1 # 0,0 값이 W인 경우
                else : # 인덱스 합이 홀수인 칸인지 검사
                    if data[x][y] != 'W' : count2 += 1 # 0,0 값이 W인 경우
                    if data[x][y] != 'B' : count1 += 1 # 0,0 값이 B인 경우
        result.append(count1) # W로 시작했을 때 칠해야하는 부분 개수 저장
        result.append(count2) # B로 시작했을 때 칠해야하는 부분 개수 저장

print(min(result)) # 칠해야하는 개수의 최소값