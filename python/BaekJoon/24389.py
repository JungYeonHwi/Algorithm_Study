def PlusOne(binNum):
    temp = 1
    result = []
    
    for idx, bi in enumerate(binNum[::-1]):

        plusResult = int(bi) + temp
        
        if plusResult > 1 : result.append(str(0))
        else : 
            result.append(str(1))
            temp = 0

        if temp == 0 : break
            
    return binNum[:32-idx-1] + result[::-1]
        
    

N = int(input())

answer = 0
binary = list(bin(N)[2:].zfill(32))

reverseBinary = [str(abs(int(bi)-1)) for bi in binary]

complement = PlusOne(binNum = reverseBinary)

for bi, co in zip(binary, complement):
    if bi != co:
        answer += 1
        
print(answer)