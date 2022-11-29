for i in range(int(input())):
    arr = input().split()
    res = "NO"
    if arr[1] == '+' and int(arr[0])+int(arr[2]) == int(arr[4]) : res = "YES"
    if arr[1] == '-' and int(arr[0])-int(arr[2]) == int(arr[4]) : res = "YES"
    print(f"Case {i+1}: {res}")