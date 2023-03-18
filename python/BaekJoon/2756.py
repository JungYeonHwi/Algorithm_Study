def cal(x,y):
    score=0
    distance=x**2+y**2
    if distance<=9 :
        score = 100
    elif distance<=36 :
        score = 80
    elif distance<=81 :
        score = 60
    elif distance<=144 :
        score = 40
    elif distance<=225 :
        score = 20
    else :
        score = 0
    return score

for _ in range(int(input())):
    nums = list(map(float, input().split()))
    p1Score, p2Score=0,0
    for i in range(3):
        p1Score += cal(nums[2*i],nums[2*i+1])
    for i in range(3,6):
        p2Score += cal(nums[2 * i], nums[2 * i + 1])
 
    if p1Score > p2Score :
        print('SCORE: %d to %d, PLAYER 1 WINS.'%(p1Score,p2Score))
    elif p1Score == p2Score :
        print('SCORE: %d to %d, TIE.'%(p1Score,p2Score))
    else :
        print('SCORE: %d to %d, PLAYER 2 WINS.'%(p1Score,p2Score))
 
