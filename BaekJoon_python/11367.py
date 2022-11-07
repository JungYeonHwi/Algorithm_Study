for _ in range(int(input())) :
    s, n = input().split()
    n = int(n)
    answer = ''
    
    if n >= 97 : answer = "A+"
    elif n >= 90 : answer = "A"
    elif n >= 87 : answer = "B+"
    elif n >= 80 : answer = "B"
    elif n >= 77 : answer = "C+"
    elif n >= 70 : answer = "C"
    elif n >= 67 : answer = "D+"
    elif n >= 60 : answer = "D"
    else: answer = "F"
    print(s, answer)