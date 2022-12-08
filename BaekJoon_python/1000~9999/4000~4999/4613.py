answer = []
while 1 :
    s = list(map(str, input()))
    if s[0] == '#' :
        for k in range(len(answer)) :
            print(answer[k])
        break
    else :
        total = 0
        for i in range(len(s)) :
            if s[i] == ' ' :
                k = 0
            else :
                k = ord(s[i]) - 64
            total = total + (i+1) * k

        answer.append(total)