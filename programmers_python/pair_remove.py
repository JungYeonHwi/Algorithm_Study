def solution(s):
    stack = []
    
    for c in s :
        if stack :
            if stack[-1] == c : stack.pop()
            else : stack.append(c)
        else : stack.append(c)
    if stack : answer = 0
    else : answer = 1
    
    return answer