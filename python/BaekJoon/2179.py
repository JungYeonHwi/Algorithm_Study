n = int(input())
a = [input() for _ in range(n)]
b = sorted(list(enumerate(a)),key = lambda x: x[1])

def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]: cnt += 1
        else: break
    return cnt

# 최장 접두사를 가진 문자열 담아둘 리스트 생성
length = [0] * (n+1)
maxlength = 0

for i in range(n-1):
    # 인접한 두개의 문자열을  check함수에 대입
    # tmp 값은 동일한 접두사의 길이
    tmp = check(b[i][1], b[i+1][1])
    # 최장 접두사 길이 갱신
    maxlength = max(maxlength, tmp)
    length[b[i][0]] = max(length[b[i][0]], tmp)
    length[b[i+1][0]] = max(length[b[i+1][0]], tmp)
    # length = [4, 0, 0, 0, 0, 4, 0, 0, 0, 0]
    
first = 0
for i in range(n):
    # 입력된 순서대로 접두사의 길이 비교
    if first == 0:
        # 만약 현재 접두사의 길이가 최장접두사라면
        if length[i] == max(length):
            # 제일 먼저 입력된 문자 출력
            first = a[i]
            print(first)
            pre = a[i][:maxlength]
    else:
    	# 다음으로 입력되었된 값들 중 최장 접두사 출력후 종료
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])
            break
