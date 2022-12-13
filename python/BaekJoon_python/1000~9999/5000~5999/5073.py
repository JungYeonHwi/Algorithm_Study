while 1 :
    arr = sorted(list(map(int, input().split())))
    if arr[0] == arr[1] == arr[2] == 0 : break
    if arr[0] + arr[1] <= arr[2] : print("Invalid")
    elif arr[0] == arr[1] == arr[2] : print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0] : print("Isosceles")
    else : print("Scalene")