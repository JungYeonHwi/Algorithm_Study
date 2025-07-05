function solution(n, slicer, num_list) {
  var answer = [];

  var [a, b, c] = slicer;

  if (n === 1) answer = num_list.slice(0, b + 1);
  else if (n === 2) answer = num_list.slice(a);
  else if (n === 3) answer = num_list.slice(a, b + 1);
  else {
    for (let i = a; i < b + 1; i += c) {
      answer.push(num_list[i]);
    }
  }

  return answer;
}
