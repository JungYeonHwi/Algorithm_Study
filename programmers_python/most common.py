from collections import Counter

def solution(array):
    
    answer = 0

    cnt = Counter(array)
    cnt.most_common()
    
    if len(cnt) <= 1 : 
        answer = cnt.most_common(1)[0][0]
    else : 
        if (cnt.most_common(2)[0][1] == cnt.most_common(2)[1][1]) : answer = -1
        else : answer = cnt.most_common(1)[0][0]
    
    return answer