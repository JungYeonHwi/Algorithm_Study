from sys import stdin

n = int(stdin.readline())

for idx in range(n) : 
    all = ""
    
    for l in stdin : 
        if l == "\n" : 
            all = all.rstrip("\n")
            break
        else : all += l.rstrip("\n")
        
    a = len(all)
    r = a - all.count("#")
    
    rda = round(r / a * 100, 1)
    
    if str(rda).split(".")[-1] == "0" : rda = int(rda)
    
    print(f"Efficiency ratio is {rda}%.")