def solution(num, total):
    answer = []
    
    sum = num * (num+1) // 2
    offset = (total - sum) // num;
    
    for i in range(1, num+1) : 
        answer.append(i+offset)
    return answer;