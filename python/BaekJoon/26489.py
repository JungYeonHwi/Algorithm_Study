n = 0

while 1 : 
    try :
        s = input()
        n += 1
    except EOFError : 
        break

print(n)