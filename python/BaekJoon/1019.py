import sys

# ans = 1부터 9까지 각가 몇번 등장했는지 세주는 배열
ans = [0] * 10

# 입력
end = int(sys.stdin.readline())

# 위 글에서 k의 역할을 하는 point
point = 1
# 문제의 조건에 따라 1부터 시작
start = 1

# calc : a,b가 9또는 0으로 끝나지 않을 때 각 자리수를 ans에 카운트 시키는 함수
def cal(x,ans,point):
    while x > 0:
        ans[x % 10] += point
        x //= 10
        

while start <= end:
    while end % 10 != 9:
        cal(end, ans, point)
        end -= 1
    if end < start:
        break
    while start % 10 != 0:
        cal(start, ans, point)
        start += 1
    start //= 10
    end //= 10
    for i in range(10):
        ans[i] += (end - start + 1) * point
    point *= 10

# 출력부
for i in range(10):
    print(ans[i], end= ' ')
