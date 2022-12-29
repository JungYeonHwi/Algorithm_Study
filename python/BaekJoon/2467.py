import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

answer = float("INF")
left = 0
right = 0

for i in range(n-1):
    current = liquids[i]

    start = i + 1
    end = n - 1

    while start <= end :
        mid = (start + end) // 2
        tmp = current + liquids[mid]

        if abs(tmp) < answer :
            answer = abs(tmp)
            left = i
            right = mid

            if tmp == 0 : break
        
        if tmp < 0 : start = mid + 1 
        else : end = mid - 1

print(liquids[left], liquids[right])