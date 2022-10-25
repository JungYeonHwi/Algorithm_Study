def solution(polynomial):
    coef = 0
    const = 0
    
    for ch in polynomial.split("+") :
        tmp = ch.strip()
        if 'x' in tmp :
            tmp = tmp.replace("x", "")
            if tmp.isdigit() :
                coef += int(tmp)
            else : coef += 1

        elif tmp.isdigit() : const += int(tmp)
        
    if coef == 1 and const != 0 : return "x" + " + " + str(const)
    elif coef == 1 and const == 0 : return "x"

    if coef == 0 and const != 0 : return str(const)
    elif coef != 0 and const == 0 : return str(coef) + "x"
    elif coef != 0 and const != 0 : return str(coef) + "x" + " + " + str(const)
    elif coef == 0 and const == 0 : return "0"