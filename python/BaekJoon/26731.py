import string

value = list(string.ascii_uppercase)

s = input()

for i in value :
    if i not in s : 
        print(i)