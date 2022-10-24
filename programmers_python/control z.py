def solution(s):
    answer = 0
    stack = []
    
    for i in (s.split()) :
        if i == 'Z' :
            if stack : stack.pop()
        else : stack.append(i)
        
    if len(stack) == 0 : return 0

    answer = eval("+".join(stack))
    
    return answer