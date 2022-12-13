while 1 :
    n = input()
    
    if (n == "EOI") : break
    else : 
        n = n.lower()
        if "nemo" in n : print("Found")
        else : print("Missing")