def solution(n):
    answer = 0

    count = 0;

    while count < n : 
        answer += 1;
        if not "3" in str(answer) and answer % 3 != 0 : count += 1

    return answer