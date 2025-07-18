function solution(today, terms, privacies) {
  const answer = [];

  const [ty, tm, td] = today.split(".").map(Number);
  const todayDate = new Date(ty, tm - 1, td);

  const termMap = {};
  for (const term of terms) {
    const [kind, months] = term.split(" ");
    termMap[kind] = Number(months);
  }

  for (let i = 0; i < privacies.length; i++) {
    const [dateStr, kind] = privacies[i].split(" ");
    const [y, m, d] = dateStr.split(".").map(Number);

    const expireDate = new Date(y, m - 1, d);
    expireDate.setMonth(expireDate.getMonth() + termMap[kind]);
    expireDate.setDate(expireDate.getDate() - 1);

    if (expireDate < todayDate) {
      answer.push(i + 1);
    }
  }

  return answer;
}
