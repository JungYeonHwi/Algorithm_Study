for _ in range(int(input())) : 
    value = input()
    s = 0
    for i in value : 
        if i == "A" : s += 4
        if i == "K" : s += 3
        if i == "Q" : s += 2
        if i == "J" : s += 1
        
print(s)