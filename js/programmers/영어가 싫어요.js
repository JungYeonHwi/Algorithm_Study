function solution(numbers) {
  var answer = 0;

  let value = "";
  let words = {
    zero: "0",
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };

  let tmpS = "";

  for (let i = 0; i < numbers.length; i++) {
    let data = numbers[i];
    tmpS += data;

    if (tmpS in words) {
      value += words[tmpS];
      tmpS = "";
    }
  }

  answer = Number(value);

  return answer;
}
