def top(n, a, b, c):
  if(n == 1) :
    print(a, c, sep = " ")
  else :
    top(n-1, a, c, b)
    top(1, a, b, c)
    top(n-1, b, a, c)

n = int(input())
print(2 ** n - 1)
if(n <= 20) :
  top(n, 1, 2, 3)