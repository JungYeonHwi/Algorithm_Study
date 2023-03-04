def findKey(f) : 
    key = 1
    while chr(ord(f) ^ key) != "C" : 
        key += 1
    return key

def de(key, s) : 
    rtn = ""
    for c in s : 
        rtn += chr(ord(c) ^ key)
    return rtn

s = input()

key = findKey(s[0])

print(de(key, s))