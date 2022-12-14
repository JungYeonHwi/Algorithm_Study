import math

def primenumber(x) :
    for i in range(2, int(math.sqrt(x) + 1)) : 
    	if x % i == 0 : 
            return False
    return True

n = int(input())

if n == 1 : print(2)
else : 
    while 1 : 
            num = str(n)
            if num == num[::-1] : 
                    if primenumber(n) : 
                        print(n)
                        break
                    else : n += 1
            else : 
                    n += 1