def solution(s):
    answer = ''
    if len(s) % 2 == 1 : 
        index = int(len(s) / 2) + 1
        answer = s[index-1]
    else : 
        index = int(len(s) / 2)
        answer = s[index-1:index+1]

    return answer