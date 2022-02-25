List = list(input())
answer = []

for i in List : 
    if i.isupper() : answer.append(i.lower())
    else : answer.append(i.upper())
    
print("".join(answer))