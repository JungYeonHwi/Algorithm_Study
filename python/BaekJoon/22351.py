s = input()

def create(start_num, total_length):
  charset = ''
  start = str(start_num)
  end = ''
  for n in range(start_num, 1000):
    if len(charset) >= total_length:
      break
    charset += str(n)
    end = str(n)
  return charset, start, end

cases = []
cases.append(create(int(s[0]), len(s))) 
if len(s) >= 2: 
  cases.append(create(int(s[0:2]), len(s)))
if len(s) >= 3:
  cases.append(create(int(s[0:3]), len(s)))

for i in range(3):
  if s == cases[i][0]:
    print(cases[i][1], cases[i][2])
    break

