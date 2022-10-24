def solution(spell, dic):
    answer = 2
    
    for i in dic : 
        dicList = list(map(str, i))
        dicList = list(set(dicList))
        print(dicList)
        
        dicList.sort()
        spell.sort()
        
        if dicList == spell : answer = 1
    
    return answeralien language