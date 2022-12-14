for _ in range(int(input())) : 
    dkagh = input()
    check = input()
    answer = ""
    
    for i in dkagh : 
        if i == " " : answer += " "
        else : 
            idx = ord(i) - 65
            answer += check[idx]
        
    print(answer)