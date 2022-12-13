List = list(map(str, input()))

s = 0

for i in range(len(List)) : 
    if (List[i] == 'A' or List[i] == 'B' or List[i] == 'C') : s += 3
    elif (List[i] == 'D' or List[i] == 'E' or List[i] == 'F') : s += 4
    elif (List[i] == 'G' or List[i] == 'H' or List[i] == 'I') : s += 5
    elif (List[i] == 'J' or List[i] == 'K' or List[i] == 'L') : s += 6
    elif (List[i] == 'M' or List[i] == 'N' or List[i] == 'O') : s += 7
    elif (List[i] == 'P' or List[i] == 'Q' or List[i] == 'R' or List[i] == 'S') : s += 8
    elif (List[i] == 'T' or List[i] == 'U' or List[i] == 'V') : s += 9
    elif (List[i] == 'W' or List[i] == 'X' or List[i] == 'Y' or List[i] == 'Z') : s += 10
    
print(s)