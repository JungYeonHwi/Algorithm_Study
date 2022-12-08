while 1 : 
    s = input()
    if s == "#" : break
    else : 
        arr = [0] * 26
        for i in s.lower() : 
            if i.isalpha() : arr[ord(i) - 97] = 1
            else : continue
        print(arr.count(1))