List = [1, 0, 0]
s = input()

for c in s :
    if c == 'A' :
        List[0], List[1] = List[1], List[0]
    elif c == 'B' :
        List[1], List[2] = List[2], List[1]
    else :
        List[0], List[2] = List[2], List[0]
print(List.index(1) + 1)