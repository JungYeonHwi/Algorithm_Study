idx = 1

while 1 : 
    t = input()
    
    if t == "0" : break
    else : 
        r, w, l = map(int, t.split(" "))
        
        diameter = 2 * r

        diagonal = (w ** 2 + l ** 2) ** 0.5
        
        if diameter >= diagonal : 
            print(f"Pizza {idx} fits on the table.")
        else : 
            print(f"Pizza {idx} does not fit on the table.")
        idx += 1