import sys

read = lambda: sys.stdin.readline().rstrip()

T = int(read())

for _ in range(T):
    N = int(read())
    A = list(map(str, read().split()))

    answer = [A[0]]

    for i in range(1, len(A)):
        left = answer[0]

        if A[i] <= left:
            answer.insert(0, A[i])
        else:
            answer.append(A[i])

    print(''.join(answer))
