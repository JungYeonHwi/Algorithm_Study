function getLCM(num1, num2) {
  let lcm = 1;

  while (true) {
    if (lcm % num1 == 0 && lcm % num2 == 0) {
      break;
    }

    lcm++;
  }

  return lcm;
}

function solution(n) {
  var answer = 0;

  if (n % 6 == 0) {
    answer = n / 6;
  } else {
    answer = getLCM(6, n) / 6;
  }

  return answer;
}
