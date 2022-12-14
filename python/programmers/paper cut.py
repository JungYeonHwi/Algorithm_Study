def solution(M, N):
    answer = 0
    
    if M == 1 and N == 1 : answer = 0
    else : 
        if M > N : 
            answer += M - 1
            answer += (N - 1) * M
        elif M <= N : 
            answer += N - 1
            answer += (M - 1) * N
    
    return answer