while 1 :
    try:
        name = input()
        cwd = {"e": "i", "i": "e", "E": "I", "I": "E"}

        nnl = [cwd[word] if word in cwd else word for word in list(name)]
        
        answer = "".join(nnl)
        
        print(answer)
        
    except EOFError :
        break