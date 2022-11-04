t = int(input())

for _ in range(t) : 
    arr = list(map(int, input().split()))
    for i in arr : 
        print(i, end=" ")
    print()
    if 18 in arr and 17 in arr : print("both")
    elif 18 in arr and 17 not in arr : print("mack")
    elif 18 not in arr and 17 in arr : print("zack")
    else : print("none")
    
    print()