while 1 : 
    arr = list(map(int, input().split()))
    if sum(arr) == 0 : break
    else : 
        print(f'{sum(arr) / 6:.1f}')