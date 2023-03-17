def check(data):
    s = []
    tag = False
    temp = ''
    for i in range(len(data)):
        if data[i] == '<':
            tag = True
        elif data[i] == '>':
            tag = False
            if temp and temp[-1] == '/':
                temp = ''
                continue
            elif s and s[-1] == temp[1:]:
                s.pop()
            else:
                s.append(temp)
            temp = ''

        if tag and data[i] == ' ' and data[i + 1] != '/':
            tag = False

        if tag and data[i] != '<':
            temp += data[i]

    if s:
        print("illegal")
    else:
        print("legal")

while 1 :
    data = input()
    if data == '#' : break
    else : check(data)