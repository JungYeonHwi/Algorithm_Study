import sys
input = sys.stdin.readline

n = int(input())
arr = tuple(map(int, input().split(" ")))

idx = arr.index(-1)

left = min(arr[:idx])
right = min(arr[idx+1:])

print(left + right)