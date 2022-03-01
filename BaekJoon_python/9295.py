T = int(input())

for i in range(T) : 
    X, Y = map(int, input().split())
    s = X + Y
    
    print("Case "+str(i+1)+":",s)