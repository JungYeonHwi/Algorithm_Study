for case in range(int(input())) :
    arr = sorted(map(int, input().split()))
    
    print(f"Case #{case+1}: ", end='')
    
    if arr[0] + arr[1] <= arr[2] : print("invalid!")
    elif arr[0] == arr[1] == arr[2] : print("equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0] : print("isosceles")
    else : print("scalene")