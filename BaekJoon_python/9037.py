def one(arr) : 
    for i in range(len(arr)) : 
        if arr[i] % 2 != 0 : arr[i] += 1
        
def game(arr) : 
    answer = 0
    
    while len(set(arr)) != 1 : 
        giveAccount = []
        answer += 1
        for i in range(len(arr)) :
            account = arr[i] // 2
            arr[i] -= account
            giveAccount.append(account)
            
        for j in range(-1, len(arr) - 1):
                arr[j+1] += giveAccount[j]
                
        one(arr)

    return answer

for _ in range(int(input())) : 
    n = int(input())
    arr = list(map(int, input().split()))
    
    one(arr)
    answer = game(arr)
    
    print(answer)