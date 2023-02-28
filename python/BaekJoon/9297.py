n = int(input())

for i in range(1, n+1) : 
    a, b = map(int, input().split())
    
    if a < b : value = str(a) + "/" + str(b)
    else : 
        if (str(a%b)) == "0" : value = str(a // b)
        else : value = str(a // b) + " " + (str(a%b) + "/" + str(b))
    
    print("Case", str(i) + ":", value)