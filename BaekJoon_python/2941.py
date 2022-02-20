N = int(input())
count = N

for i in range(N) : 
    word = input()
    for k in range(len(word) - 1) : 
        if (word[k] == word[k+1]) : pass
        elif (word[k] in word[k+1:]) : 
            count -= 1
            break
        
print(count)