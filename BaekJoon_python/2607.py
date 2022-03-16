n = int(input()) # 단어의 개수 n을 입력 받는다
firstWord = list(input()) # 첫 번째 단어를 입력 받는다

answer = 0 # 개수 확인하는 변수 초기화한다

for _ in range(n-1) : # 첫 번째 단어를 제외한 n-1개의 단어를 확인해본다
    compareWord = firstWord[:] # 첫 번째 단어를 단어마다 확인하기 위해 저장한다
    
    checkWord = list(input()) # 확인할 단어를 입력 받는다 (n-1개 입력 받는다)
    
    for _ in range(len(checkWord)) : # 확인할 단어의 길이만큼 확인한다
        w = checkWord.pop(0) # 확인할 단어의 맨 마지막 값을 w에 할당하고, checkWord에서 삭제
        
        if w in compareWord : compareWord.remove(w) # 첫 번째 단어에 w가 있으면, w값을 첫 번째 단어에서 삭제
        else : checkWord.append(w) # 첫 번째 단어에 w가 없으면, checkWord에 추가
        
    # 연산 후 남은 길이들을 확인
    a = len(compareWord) # 첫 번째 단어의 남은 길이를 a라고 한다
    b = len(checkWord) # 확인할 단어의 남은 길이를 b라고 한다

    # 길이들이 0 또는 1일 경우에만 개수가 증가할 수 있다
    if (a == 0 and b == 0) or (a == 1 and b == 0) or (a == 0 and b == 1) or (a == 1 and b == 1) : answer += 1
    
print(answer) # 정답을 출력한다