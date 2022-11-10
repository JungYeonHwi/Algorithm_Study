for i in range(int(input())):
    a,b=map(int,input().split())
    
    print("Yes" if 0<=a<=23 and 0<=b<=59 else "No", end=" ")
    
    if a==2 :
        print("Yes" if 1<=b<=29 else "No")
    elif a in [1,3,5,7,8,10,12] :
        print("Yes" if 1<=b<=31 else "No")
    elif a in [4,6,9,11] :
        print("Yes" if 1<=b<=30 else "No")
    else :
        print("No")