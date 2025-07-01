function solution(myString) {
    var answer = '';
    
    for (let i = 0; i < myString.length; i++) {
        if(myString[i] === 'a' || myString[i] === 'A') answer += 'A';
        else answer += myString[i].toLowerCase();
    }
    
    return answer;
}ㅁ