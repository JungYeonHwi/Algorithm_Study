n = int(input())

dict = {
    1 : "Yakk",
    2 : "Doh",
    3 : "Seh",
    4 : "Ghar",
    5 : "Bang",
    6 : "Sheesh"
}

for i in range(1, n+1) : 
    arr = list(map(int, input().split()))
    
    arr.sort()
    arr = arr[::-1]
    
    a = arr[0]
    b = arr[1]
    
    value = ""
    
    if a == b == 1 : value = "Habb Yakk"
    elif a == b == 2 : value = "Dobara"
    elif a == b == 3 : value = "Dousa"
    elif a == b == 4 : value = "Dorgy"
    elif a == b == 5 : value = "Dabash"
    elif a == b == 6 : value = "Dosh"
    else : 
        value = dict[a] + " " + dict[b]
    if a == 6 and b == 5 : value = "Sheesh Beesh"
    
    print("Case " + str(i) + ": " + value)   
    