import sys
vowel = {'a', 'e', 'i', 'o', 'u'}
while 1 :
	test = sys.stdin.readline().rstrip()
	if test == 'end' : break
 
	pw = list(test)
	vFlag = 0
	vCount = 0
	cCount = 0
	err = 0
	for i in range(len(pw)) :
		if i > 0 :
			if pw[i] == pw[i-1] :
				if pw[i] != 'e' and pw[i] != 'o':
					err = 1
					break
		if pw[i] in vowel :
			vFlag = 1
			vCount += 1
			cCount = 0
			if vCount == 3 :
				err = 1
				break
		else :
			vCount = 0
			cCount += 1
			if cCount == 3 :
				err = 1
				break
	
	if (err != 1) and (vFlag == 1) : print("<"+ test +"> is acceptable.")
	else : print("<" + test + "> is not acceptable.")