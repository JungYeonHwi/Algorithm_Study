function real(item) {
  let ahrt = Math.floor(item / 100);
  let skajwl = item % 100;
  return Number(ahrt) * 60 + Number(skajwl);
}

function solution(schedules, timelogs, startday) {
  var answer = 0;
  let n = schedules.length;
  let arr = [];

  for (let i = 0; i < n; i++) {
    let check = true;
    let want = real(schedules[i]);
    let max = want + 10;

    for (let k = 0; k < 7; k++) {
      let day = (k + startday) % 7;
      if (day === 6 || day === 0) continue;
      else {
        let workTime = real(timelogs[i][k]);
        if (workTime > max) {
          check = false;
          break;
        }
      }
    }

    if (check) answer += 1;
  }

  return answer;
}
