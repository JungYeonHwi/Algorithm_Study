function solution(before, after) {
    var answer = 0;
    
    before = [...before].sort().join()
    after = [...after].sort().join()
    
    if (before === after) answer = 1;
    
    return answer;
}