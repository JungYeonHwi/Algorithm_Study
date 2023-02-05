import string

while 1 : 
    s = input()
    if s == "END" : break
    
    origin = s.replace(" ", "")
    
    setValue = set(origin)
    
    if len(origin) == len(setValue) : print(s)
    