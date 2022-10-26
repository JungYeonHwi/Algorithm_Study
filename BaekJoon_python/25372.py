n = int(input())

for _ in range(n) : 
    arr = list(map(str, input()))
    if len(arr) >= 6 and len(arr) <= 9 : print("yes")
    else : print("no")