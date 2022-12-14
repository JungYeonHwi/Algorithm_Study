function solution(array, n) {
  var answer = 0;

  let arr = [];

  array.forEach((item) => {
    arr.push(Math.abs(item - n));
  });

  const min = Math.min(...arr);

  if (arr.indexOf(min) !== arr.lastIndexOf(min)) {
    const indexOne = arr.indexOf(min);
    const indexTwo = arr.lastIndexOf(min);

    answer = Math.min(array[indexOne], array[indexTwo]);
  } else {
    const idx = arr.indexOf(Math.min(...arr));
    answer = array[idx];
  }

  return answer;
}
