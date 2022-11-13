reflect = ['b', 'd', 'p', 'q', 'i', 'o', 'v', 'w', 'x']

while 1 : 
    word = input()
    
    if word == "#" : break

    answer = ''
    
    for i in word : 
        if i not in reflect : 
            answer = "INVALID"
            break

        else : 
            if i == "b" : answer += "d"
            elif i == "d" : answer += "b"
            elif i == "p" : answer += "q"
            elif i == "q" : answer += "p"
            else : 
                answer += i

    if answer != "INVALID" : 
        print(answer[::-1])
    else : print(answer)