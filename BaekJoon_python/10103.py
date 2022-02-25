N = int(input())
AScore = 100
BScore = 100

for i in range(N) :  
    A, B = map(int, input().split())

    if (A > B) : BScore -= A
    elif (A < B) : AScore -= B
    
print(AScore)
print(BScore)