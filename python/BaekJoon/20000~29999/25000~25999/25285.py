n = int(input())

for _ in range(n) : 
    h, w = map(int, input().split())
    hh = h * h
    bmi = w / hh * 10000
    # print(bmi)
    if h < 140.1 : print(6)
    elif h < 146 : print(5)
    elif h < 159 : print(4)
    elif h < 161 : 
        if bmi >= 16.0 and bmi < 35.0 : print(3)
        elif bmi < 16.0 or bmi >= 35.0 : print(4)
    elif h < 204 : 
        if bmi >= 20.0 and bmi < 25.0 : print(1)
        elif bmi >= 18.5 and bmi < 20.0 : print(2)
        elif bmi >= 25.0 and bmi < 30.0 : print(2)
        elif bmi >= 16.0 and bmi < 18.5 : print(3)
        elif bmi >= 30.0 and bmi < 35.0  : print(3)
        elif bmi < 16.0 or bmi >= 35.0 : print(4)
    else : print(4)
