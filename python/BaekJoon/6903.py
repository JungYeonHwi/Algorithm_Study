t = int(input())
s = int(input())
h = int(input())

for i in range(t) : 
    print(("*" + " " * s) * 3)
    
print("*" * ((s + 1) * 2 + 1))

for k in range(h) : 
    print(" " * (s + 1) + "*")