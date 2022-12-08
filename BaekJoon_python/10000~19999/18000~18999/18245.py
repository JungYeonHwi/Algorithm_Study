value = 1

while 1 : 
    s = input()
    answer = ''
    if s == "Was it a cat I saw?" : break
    else : 
        for i in range(0, len(s), value+1) :
            answer += s[i]
        print(answer)
        value += 1
