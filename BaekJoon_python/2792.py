import sys

n, m = list(map(int, sys.stdin.readline().split()))

jewels = []
end = 0

for _ in range(m) :
    value = int(sys.stdin.readline().rstrip())
    jewels.append(value)
    end = max(end, value)

answer = end

start = 1

while start <= end :
    mid = (start + end) // 2

    ppj = 0
    for jewel in jewels :
        quotient = jewel // mid
        remainder = jewel % mid

        ppj += quotient
        if remainder > 0 : ppj += 1

    if ppj > n : start = mid + 1
    else :
        answer = min(answer, mid)
        end = mid - 1

print(answer)