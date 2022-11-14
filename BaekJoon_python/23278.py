N, L, H = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
answer = sum(arr[L : N - H]) / (N - L - H)
print(answer)
