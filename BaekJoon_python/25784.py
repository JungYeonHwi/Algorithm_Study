arr = list(map(int, input().split()))

arr.sort()

if arr[0] + arr[1] == arr[2] : print(1)
elif arr[0] * arr[1] == arr[2] : print(2)
else : print(3)
