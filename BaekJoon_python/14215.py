arr = sorted(map(int, input().split()))
answer = arr[0] + arr[1] + min(arr[2], arr[0] + arr[1] - 1)
print(answer)