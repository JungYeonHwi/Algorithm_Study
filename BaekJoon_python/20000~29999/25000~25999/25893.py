n = int(input())

for _ in range(n) : 
    arr = list(map(int, input().split()))
    check = 0
    
    for i in arr : 
        if i >= 10 : check += 1
        print(i, end = " ")
    print()
    
            
    if check == 3 : print("triple-double")
    elif check == 2 : print("double-double")
    elif check == 1 : print("double")
    else : print("zilch")
    
    print()