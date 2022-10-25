def solution(quiz):
    answer = []
    
    quizList = []
    
    for i in quiz : 
        quizList = list(map(str, i.split(" ")))
        check = quizList[:3:]
        check = "".join(check)
        
        if eval(check) == int(quizList[-1]) : answer.append("O")
        else : answer.append("X")
    
    return answer