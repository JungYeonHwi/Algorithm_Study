def solution(answers):
    answer = []
    
    one = []; two = [2, 1, 2, 3, 2, 4, 2, 5]; three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    oneCheck = 0; twoCheck = 0; threeCheck = 0
    
    for i in range(1, len(answers)+1) : 
        if i%5 == 0 : one.append(5)
        elif i%5 < 5 : one.append(i%5)

        if i%8 == 0 : two.extend([2, 1, 2, 3, 2, 4, 2, 5])
        if i%10 == 0 : three.extend([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
        
    two = two[:len(answers):]
    three = three[:len(answers):]
    
    for q, w, e, i in zip(one, two, three, answers) :
        if i == q : oneCheck += 1
        if i == w : twoCheck += 1
        if i == e : threeCheck += 1

    maxList = []
    maxList.append(oneCheck)
    maxList.append(twoCheck)
    maxList.append(threeCheck)
    
    maxList.sort(reverse=True)
    
    if maxList[0] == oneCheck : answer.append(1)
    if maxList[0] == twoCheck : answer.append(2)
    if maxList[0] == threeCheck : answer.append(3)
    
    return answer