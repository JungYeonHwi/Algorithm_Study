from sys import stdin

n = int(stdin.readline())

for _ in range(n) : 
    temp = ''
    
    for line in stdin : 
        if line == "\n" : 
            temp = temp.rstrip("\n")
            break
        else : temp += temp.rstrip("\n")
    
    l = len(temp)
    r = l - temp.count("#")
    rda = round(r / l * 100, 1)
    
    if str(rda).split(".")[-1] == "0" : rda = int(rda)

    print(f"Efficiency ratio is {rda}%.")