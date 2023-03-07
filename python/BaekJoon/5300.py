n = int(input())
cnt = 0

if n % 6 == 0 : 
    for i in range(1, n+1) : 
        print(i)
        cnt += 1
        if cnt % 6 == 0 : 
            print("Go!")
            cnt = 0
else : 
    for i in range(1, n+1) : 
        print(i)
        cnt += 1
        if cnt % 6 == 0 : 
            print("Go!")
            cnt = 0
    print("Go!")
        