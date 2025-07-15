function solution(numbers, hand) {
  var answer = "";

  let keypad = [
    ["*", [0, 0]],
    [0, [1, 0]],
    ["#", [2, 0]],
    [7, [0, 1]],
    [8, [1, 1]],
    [9, [2, 1]],
    [4, [0, 2]],
    [5, [1, 2]],
    [6, [2, 2]],
    [1, [0, 3]],
    [2, [1, 3]],
    [3, [2, 3]],
  ];

  let currentLeft = [0, 0];
  let currentRight = [2, 0];

  for (let i = 0; i < numbers.length; i++) {
    let find = keypad.find((item) => item[0] === numbers[i]);
    let [num, [x, y]] = find;

    if (num === 1 || num === 4 || num === 7) {
      answer += "L";
      currentLeft = [x, y];
    } else if (num === 3 || num === 6 || num === 9) {
      answer += "R";
      currentRight = [x, y];
    } else {
      let leftDistance =
        Math.abs(currentLeft[0] - x) + Math.abs(currentLeft[1] - y);
      let rightDistance =
        Math.abs(currentRight[0] - x) + Math.abs(currentRight[1] - y);

      if (leftDistance < rightDistance) {
        answer += "L";
        currentLeft = [x, y];
      } else if (leftDistance > rightDistance) {
        answer += "R";
        currentRight = [x, y];
      } else {
        if (hand === "left") {
          answer += "L";
          currentLeft = [x, y];
        } else {
          answer += "R";
          currentRight = [x, y];
        }
      }
    }
  }

  return answer;
}
