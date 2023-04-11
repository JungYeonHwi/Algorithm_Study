party_people = [input() for _ in range(5)]
photo = [''] * 5	

for i in range(len(party_people[0])) :
  
    arr = party_people[0][i] + party_people[1][i] + party_people[2][i] + party_people[3][i] + party_people[4][i]

    if arr == '.omln' :	
        photo[0] += 'o'
        photo[1] += 'w'
        photo[2] += 'l'
        photo[3] += 'n'
        photo[4] += '.'
    elif arr == 'owln.' :	
        photo[0] += '.'
        photo[1] += 'o'
        photo[2] += 'm'
        photo[3] += 'l'
        photo[4] += 'n'
    else :	
        photo[0] += '.'
        photo[1] += '.'
        photo[2] += 'o'
        photo[3] += 'L'
        photo[4] += 'n'

for p in photo :
    print(p)