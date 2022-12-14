function solution(quiz) {
  var answer = [];

  quiz.forEach((item) => {
    const oneQuiz = item.split(" ");

    const X = Number(oneQuiz[0]);
    const Y = Number(oneQuiz[2]);

    let calc = 0;

    if (oneQuiz[1] === "+") {
      calc = X + Y;
    }

    if (oneQuiz[1] === "-") {
      calc = X - Y;
    }

    const result = Number(oneQuiz[4]);

    if (calc === result) {
      answer.push("O");
    }

    if (calc !== result) {
      answer.push("X");
    }
  });

  return answer;
}
