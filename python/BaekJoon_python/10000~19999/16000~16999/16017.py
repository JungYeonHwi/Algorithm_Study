arr = [int(input()) for _ in range(4)]
if arr[0] in [8,9] and arr[-1] in [8, 9] and arr[1] == arr[2] : print("ignore")
else : print("answer")