from string import ascii_uppercase

def Java_To_C(v) :
    tmp = v[0]
    if tmp.isupper() :
        return 'Error!'
    for i in range(1, len(v)) :
        if v[i].isupper() :
            tmp += '_'
            tmp += v[i].lower()
        else :
            tmp += v[i]

    return tmp

def C_to_Java() :
    for i in range(1, len(list(s))) :
        if s[i-1] == s[i] == '_' :
            return 'Error!'
    if s[0] == '_' or s[-1] == '_':
        return 'Error!'
    arr = s.split('_')

    for i in arr :
        if not i.isalnum() :
            return 'Error!'
        if i.lower() != i :
            return "Error!"
    for i in range(len(arr)) :
        if arr[i][0].lower() != arr[i][0] :
            return 'Error!'
    for i in range(1, len(arr)) :
        arr[i] = arr[i].capitalize()
    return ''.join(arr)

answer = []
java_result_list = []

s = input()
uppercase = list(ascii_uppercase)

if '_' in s :
    if len(answer) == 0 :
        answer.append(C_to_Java())
else :
    if s.lower() == s :
        print(s)
    else :
        for i in uppercase :
            if i in s :
                if len(answer) == 0:
                    answer.append(Java_To_C(s))

if len(answer) > 0:
    print(''.join(answer))