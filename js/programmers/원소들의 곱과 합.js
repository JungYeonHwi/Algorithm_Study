function solution(num_list) {
  var answer = 0;

  let rhq = num_list.reduce((a, b) => a * b);
  let ghf = num_list.reduce((a, b) => a + b) * num_list.reduce((a, b) => a + b);

  return (answer = rhq > ghf ? 0 : 1);
}
