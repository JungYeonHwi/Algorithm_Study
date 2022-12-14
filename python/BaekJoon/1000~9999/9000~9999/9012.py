n = int(input())

for _ in range(n) : 
    s = input()
    answer = 0
    for i in s :
        if i == '(' : answer += 1
        elif i == ')' : answer -= 1

        if answer < 0 : 
            print("NO")
            break
    
    if answer > 0 : print("NO")
    elif answer == 0 : print("YES")
            