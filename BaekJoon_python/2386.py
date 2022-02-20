while(1) :
    value = input() 
    if (value == '#') : break
    
    letter = value[0]
    sentence = value[2:].lower()
     
    answer = sentence.count(letter)
    print(letter, answer)