def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표료 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    leftPos = dic['*']
    rightPos = dic['#']
    
    for i in numbers :
        now = dic[i]
        # 1, 4, 7을 누르는 경우 무조건 왼손
        if i in [1, 4, 7] : 
            answer += 'L'
            leftPos = now
            
        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif i in [3, 6, 9] :
            answer += 'R'
            rightPos = now
            
        # 2, 5, 8, 0을 누르는 경우
        else :
            LeftDis = 0
            rightDis = 0
            
            # 좌표 거리
            for a, b, c in zip(leftPos, rightPos, now) :
                LeftDis += abs(a-c)
                rightDis += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if LeftDis < rightDis :
                answer += 'L'
                leftPos = now
                
            # 오른손이 더 가까운 경우
            elif LeftDis > rightDis :
                answer += 'R'
                rightPos = now
            
            # 두 거리가 같은 경우
            else :
                # 왼손잡이 경우
                if hand == 'left' :
                    answer += 'L'
                    leftPos = now
                    
                # 오른손잡이 경우
                else :
                    answer += 'R'
                    rightPos = now
    
    return answer