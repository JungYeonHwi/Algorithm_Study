import string

arr = list(string.ascii_uppercase)

for _ in range(int(input())) : 
    s = input()
    answer = 0
    
    s = s.replace(" ", "")
    
    for i in s : 
        answer += arr.index(i) + 1
    
    if answer == 100 : print("PERFECT LIFE")
    else : print(answer)