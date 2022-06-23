from itertools import permutations

n = int(input())
signs = input().split()
nums = [0,1,2,3,4,5,6,7,8,9]

permute = permutations(nums, n+1)
result = []

for per in permute :
  flag = True
  for i in range(len(signs)) :
    if signs[i] == '<' :
      if per[i] < per[i+1] : continue
      else : 
        flag = False
        break
    else :
      if per[i] > per[i+1] : continue
      else : 
        flag = False
        break
  if flag : result.append(per)

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))