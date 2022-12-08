from itertools import permutations # 순열 라이브러리 이용

n = int(input()) # 부등호 문자 개수
signs = input().split() # 부등호 저장
nums = [0,1,2,3,4,5,6,7,8,9] # 순열을 이용할 숫자 list

permute = permutations(nums, n+1) # 부등호는 가운데 있기 때문에 순열은 부등호 개수보다 1개 더 많이 하여 순열 표현
result = [] # 정답을 저장할 list

for per in permute : # 순열 조합들 모두 확인
  flag = True # 부등호에 맞는 것인지 확인하기 위한 변수
  for i in range(len(signs)) : # 부등호 길이만큼 확인
    if signs[i] == '<' : # 부등호가 '<' 라면
      if per[i] < per[i+1] : continue # 순열 조합도 '<' 확인하여 맞다면 계속
      else : # 틀리다면
        flag = False # 틀렸다고 표시
        break # 멈춤
    else : # 부등호가 '>' 라면
      if per[i] > per[i+1] : continue # 순열 조합도 '>' 확인하여 맞다면 계속
      else : # 틀리다면 
        flag = False # 틀렸다고 표시
        break # 멈춤
  if flag : result.append(per) # 틀리지 않았다면 해당 순열을 저장

print(''.join(map(str,list(max(result))))) # 가장 큰 숫자의 순열
print(''.join(map(str,list(min(result))))) # 가장 작은 숫자의 순열