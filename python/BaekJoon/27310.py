s = input()

zhffhs = 0
djsejqk = 0

for i in s : 
    if i == ":" : zhffhs += 1
    elif i == "_" : djsejqk += 1
    
print(len(s) + zhffhs + djsejqk * 5)