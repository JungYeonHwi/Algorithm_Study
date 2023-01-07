import sys
input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))
arr = [0]

for case in cases:
    if arr[-1] < case :
        arr.append(case)
    else:
        left = 0
        right = len(arr)

        while left < right :
            mid = (right + left) // 2
            if arr[mid]<case:
                left = mid+1
            else :
                right = mid
        arr[right] = case

print(len(arr)-1)