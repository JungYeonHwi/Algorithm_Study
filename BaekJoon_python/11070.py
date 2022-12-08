for _ in range(int(input())) :
    s = input().lower()
    tmp = [1] * 26
    for i in s :
        if ord(i) > 96 and ord(i) < 123 : tmp[ord(i)-97] = 0
    if sum(tmp) == 0 : print("pangram")
    else :
        print("missing ", end='')
        for i in range(len(tmp)) :
            if tmp[i] == 1 : print(chr(i+97), end='')
        print()
