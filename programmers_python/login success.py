def solution(id_pw, db):
    answer = "wrong pw"
    
    idList = []
    pwList = []

    for i in range(len(db)) : 
        if (id_pw[0] == db[i][0]) : idList.append(i)
        if (id_pw[1] == db[i][1]) : pwList.append(i)
        
    if len(idList) == 0 : answer = "fail"
    else :
        for i in idList : 
            for j in pwList : 
                if i == j : answer = "login"
    
    return answer