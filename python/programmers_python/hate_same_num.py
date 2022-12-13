def solution(arr):
    arr.append(1000001)
    answer = []
    
    for i in range(len(arr)-1) : 
        
        if arr[i] != arr[i+1] : 
            print(arr[i], arr[i+1])
            answer.append(arr[i])
    
    return answer