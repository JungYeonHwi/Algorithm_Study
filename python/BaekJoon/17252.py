n = int(input())
good = True
if n == 0 :
    good = False
   
while n > 0 :
	if n % 3 == 2 :
		good = False
	n //= 3

if good :
	print("YES")
else :
	print("NO")