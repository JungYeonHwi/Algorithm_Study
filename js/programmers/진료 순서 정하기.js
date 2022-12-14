function solution(emergency) {
  var answer = [];

  let emergencyCopy = emergency.slice();

  emergencyCopy.sort(function (a, b) {
    return a - b;
  });

  emergencyCopy.reverse();

  for (let j = 0; j < emergency.length; j++) {
    for (let i = 0; i < emergencyCopy.length; i++) {
      if (emergency[j] == emergencyCopy[i]) {
        answer.push(i + 1);
      }
    }
  }

  return answer;
}
