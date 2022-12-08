arr = sorted(map(int, input().split()))
if arr[0] == arr[1] == arr[2] : print(2)
elif arr[0]**2 + arr[1]**2 == arr[2]**2 : print(1)
else : print(0)