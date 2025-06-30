function solution(rank, attendance) {
  var answer = 0;

  let remain = [];

  for (let i = 0; i < attendance.length; i++) {
    if (attendance[i]) remain.push(rank[i]);
  }

  remain = remain.sort((a, b) => a - b);
  answer =
    rank.indexOf(remain[0]) * 10000 +
    rank.indexOf(remain[1]) * 100 +
    rank.indexOf(remain[2]);

  return answer;
}
