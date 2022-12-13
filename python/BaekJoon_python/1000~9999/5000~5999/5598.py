transformed = input()
result = ''

for cha in transformed:

    cha = ord(cha) - 65
    cha = cha - 3 + 26
    cha = cha % 26
    cha = cha + 65
    
    result += chr(cha)
    
print(result)