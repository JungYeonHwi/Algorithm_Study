import math

n = int(input())

words = []
dict = {}

for _ in range(n) : 
    words.append(input())
    
for word in words :
  squareRoot = len(word) - 1 # 맨 뒤의 자리가 1의 자리이기 때문에 -1을 해줘야 함
  
  for c in word :
    if c in dict : dict[c] += math.pow(10, squareRoot) # 값이 있는 경우 더하기
    else : dict[c] = math.pow(10, squareRoot) # 값이 없는 경우 그대로

    squareRoot -= 1 # 제곱근 감소

dict = sorted(dict.values(), reverse=True) # 큰값부터 쓰기 위해 정렬

result = 0
m = 9 # 제일 큰 수부터 차례로 내려가며 알파벳에 배치

for value in dict :
  result += value * m 
  m -= 1

print(int(result))