def solution(my_string):
    answer = ''
    capList = [0 for i in range(26)]
    lowList = [0 for i in range(26)]
    black = [0]
    
    for i in my_string : 
        if i.isupper() : 
            capList[ord(i)-65] += 1
            if capList[ord(i)-65] == 1 : answer += i
        if i.islower() : 
            lowList[ord(i)-97] += 1
            if lowList[ord(i)-97] == 1 : answer += i
        if i == " " : 
            black[0] += 1
            if black[0] == 1 : answer += " "

    
    return answer