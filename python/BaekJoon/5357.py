for _ in range(int(input())):
    s = input()
    
    ds = [s[0]]
    
    for word in s[1:]:
        if word != ds[-1]:
            ds.append(word)
            
    answer = "".join(ds)
    
    print(answer)

