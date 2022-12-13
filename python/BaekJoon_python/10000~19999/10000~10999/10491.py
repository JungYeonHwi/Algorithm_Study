import sys

for L in sys.stdin : 
    l = L.lower()
    
    if "problem" in l : print("yes")
    else : print("no")