import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
X = int(input())
arr.sort()

left, right = 0, N - 1
answer = 0

while left < right :
    tmp = arr[left] + arr[right]
    if tmp == X: answer += 1
    if tmp < X :
        left += 1
        continue
    right -= 1
print(answer)