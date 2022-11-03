tc = int(input())

for _ in range(tc):
    n, m = list(map(int, input().split( )))
    arr = list(map(int, input().split( )))
    idx = list(range(len(arr)))
    idx[m] = 'target'

    order = 0
    
    while 1 : 
        if arr[0]==max(arr) :
            order += 1
            
            if idx[0]=='target' :
                print(order)
                break
            else :
                arr.pop(0)
                idx.pop(0)

        else :
            arr.append(arr.pop(0))
            idx.append(idx.pop(0))        