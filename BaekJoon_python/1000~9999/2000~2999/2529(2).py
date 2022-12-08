def numCheck(x, y, op) : # 부등호 기호를 확인할 함수
  if op == '<' : # 부등호가 '<' 라면
    if x > y : return False # 숫자들이 '>' 가 되면 false
  if op == '>' : # 부등호가 '<' 라면
    if x < y : return False # 숫자들이 '<' 가 되면 false
  return True # 부등호 기호에 맞다면 true

def re(index, num) : # 숫자들을 확인할 재귀 함수
  if index == n+1 : # 부등호가 n개 입력되니까 숫자는 n+1개 필요
    result.append(num) # 숫자가 n+1개가 되면 결과 저장
    return # 종료
  
  for i in range(10) : # 숫자들 확인
    if check[i] : continue # 해당 숫자를 이미 사용했다면 pass

    if index == 0 or numCheck(num[index-1], str(i), signs[index-1]) : # 숫자 개수가 0개 또는 부등호 기호들에 맞게 확인해서 true라면
      check[i] = True # 해당 숫자들을 사용함을 표시
      re(index + 1, num+str(i)) # 반복
      check[i] = False # 숫자들 사용함 취소

n = int(input()) # 부등호 문자 개수
signs = input().split() # 부등호 저장

result = [] # 정답을 저장할 list
check = [False] * 10 # 해당 숫자를 사용했는지 안 했는지 체크

re(0, '') # 재귀 함수 시작

result.sort() # 정답 list를 정렬
print(result[-1]) # list의 [-1]은 제일 큰 값
print(result[0]) # list의 [0]은 제일 작은 값