while 1 : 
    try : 
        n, s = map(int, input().split())
        answer = s // (n + 1)
        print(answer)
    except EOFError : break