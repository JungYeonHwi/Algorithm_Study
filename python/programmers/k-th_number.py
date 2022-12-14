def solution(array, commands):
    arr = []
    answer = []
    for i in range(len(commands)) :
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        arr = array[a-1:b]
        arr.sort()
        answer.append(arr[c-1])
    return answer