import sys
from collections import deque

N = int(sys.stdin.readline())
arr = list()
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())

for i in range(N):
    dq = deque(arr[i])
    while True:
        dq.append(dq.popleft())
        save = "".join(dq)
        if save == arr[i]:
            break

        if save in arr:
            idx = arr.index(save)
            arr.pop(idx)
            arr.insert(idx, arr[i])

arr = set(arr)
print(len(arr))