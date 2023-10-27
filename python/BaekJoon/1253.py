import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())

A = list(map(int, read().split()))
A.sort()

answer = 0

for i in range(N):
    temp = A[:i] + A[i+1:]
    start, end = 0, len(temp) - 1

    while start < end:
        total = temp[start] + temp[end]
        if total == A[i]:
            answer += 1
            break
        elif total < A[i]:
            start += 1
        else:
            end -= 1

print(answer)
