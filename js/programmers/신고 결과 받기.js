function solution(id_list, report, k) {
  var answer = [];
  var total = [];

  for (let i = 0; i < id_list.length; i++) {
    total.push([""]);
    answer.push(0);
  }

  for (let i = 0; i < report.length; i++) {
    let val = report[i].split(" ");
    let [a, b] = [val[0], val[1]];

    let index = id_list.indexOf(b);
    if (!total[index].includes(a)) total[index].push(a);
  }

  for (let i = 0; i < total.length; i++) {
    total[i].shift();
    let c = total[i].length;

    if (c >= k) {
      for (let j = 0; j < c; j++) {
        let index = id_list.indexOf(total[i][j]);
        answer[index] += 1;
      }
    }
  }

  return answer;
}
