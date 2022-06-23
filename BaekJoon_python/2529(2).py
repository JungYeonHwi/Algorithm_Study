def numCheck(x, y, op) :
  if op == '<' :
    if x > y : return False
  if op == '>' :
    if x < y : return False
  return True

def re(index, num) :
  if index == n+1 : # 부등호가 n개 입력되니까 숫자는 n+1개 필요
    result.append(num)
    return
  
  for i in range(10) :
    if check[i] : continue # 해당 숫자를 이미 사용했다면 pass

    if index == 0 or numCheck(num[index-1], str(i), signs[index-1]) :
      check[i] = True
      re(index + 1, num+str(i))
      check[i] = False

n = int(input())
signs = input().split()

result = []
check = [False] * 10 # 해당 숫자를 사용했는지 안 했는지 체크

re(0, '')

result.sort()
print(result[-1])
print(result[0])