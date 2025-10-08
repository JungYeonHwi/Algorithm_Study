function solution(emergency) {
  const copiedEmergency = [...emergency].sort((a, b) => b - a);
  var answer = new Array(emergency.length).fill(0);

  let k = 1;

  for (let i = 0; i < copiedEmergency.length; i++) {
    let val = emergency.indexOf(copiedEmergency[i]);
    answer[val] = k;
    k += 1;
  }

  return answer;
}
