import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

step = M
window = sum(numbers[:step])
answer = window
for i in range(step, N):
    window += numbers[i] - numbers[i - step]
    answer = max(answer, window)

print(answer)