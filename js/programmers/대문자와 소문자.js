function solution(my_string) {
  var answer = "";

  for (let i = 0; i < my_string.length; i++) {
    let data = my_string[i];

    let up = data.toUpperCase();
    let low = data.toLowerCase();

    if (data == up) {
      answer += data.toLowerCase();
    } else if (data == low) {
      answer += data.toUpperCase();
    }
  }

  return answer;
}
