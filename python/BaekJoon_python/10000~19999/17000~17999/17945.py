A, B = map(int, input().split())
arr = []
for i in range(-1000, 10001):
    if i * (2 * A - i) == B:
        arr = list(set([-i, -(2*A-i)]))
print(*sorted(arr))