arr = list(map(int, input().split()))

if arr[0] == arr[1] and arr[0] == arr[-1] : print("*")
elif arr[0] != arr[1] and arr[0] != arr[-1] and arr[1] == arr[-1] : print("A")
elif arr[1] != arr[0] and arr[1] != arr[-1] and arr[0] == arr[-1] : print("B")
else : print("C")