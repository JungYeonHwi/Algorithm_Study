def roundUp(num):
    if num - int(num) < 0.5 : return int(num)
    else : return int(num) + 1

N, emotion = map(int, input().split())
prob = list(map(float, input().split()))
probGood = [1-emotion]
probBad = [emotion]

for i in range(N) :
    probGood.append(probGood[i] * prob[0] + probBad[i] * prob[2])
    probBad.append(probGood[i] * prob[1] + probBad[i] * prob[3])
print(roundUp(probGood[-1] * 1000))
print(roundUp(probBad[-1] * 1000))
