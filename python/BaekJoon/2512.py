N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start, end = 0, max(budget)
total = 0

if sum(budget) >= end :
	print(max(budget))
else :
    while start <= end :
        mid = (start+end) // 2

        total = 0
        for i in budget :
            total += min(mid, i)

        if total > M : end = mid - 1
        else : start = mid + 1
    print(mid)