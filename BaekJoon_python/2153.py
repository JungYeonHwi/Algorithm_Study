import math

def primenumber(x) :
    for i in range(2, int(math.sqrt(x) + 1)) : 
    	if x % i == 0 : 
            return False
    return True

s = input()
n = 0
for i in s :
    if i.isupper() : 
        n += ord(i) - 38
    else : 
        n += ord(i) - 96
        
        
if primenumber(n) : print("It is a prime word.")
else : print("It is not a prime word.")