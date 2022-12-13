for _ in range(int(input())) : 
    n = int(input())
    arr = []
    for i in range(n) : 
        arr.append(int(input()))
        
    majorityVotes = int(sum(arr) / 2)
    maxVotedCandidate = max(arr)
    idx = arr.index(maxVotedCandidate) + 1
    
    if arr.count(maxVotedCandidate) >= 2 : print("no winner")
    else : 
        if maxVotedCandidate > majorityVotes : print("majority winner", str(idx))
        else : print("minority winner", str(idx))