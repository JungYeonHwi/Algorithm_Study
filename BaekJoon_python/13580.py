arr = sorted(list(map(int, input().split())))

if arr[0] == arr[1] : print("S")
elif arr[1] == arr[2] : print("S")
elif arr[0] + arr[1] == arr[2] : print("S")
else : print("N")