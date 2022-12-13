arr = [int(input()) for _ in range(5)]
X = arr[4] * arr[0]
Y = arr[1] + arr[3] * max(0, arr[4] - arr[2])

print(min(X, Y))