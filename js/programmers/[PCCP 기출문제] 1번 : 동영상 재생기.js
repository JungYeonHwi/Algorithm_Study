function formatted(item) {
  return Number(item[0]) * 60 + Number(item[1]);
}

function reformat(item) {
  let ahrt = parseInt(item / 60);
  let skajwl = item - 60 * ahrt;

  value = String(ahrt).padStart(2, "0") + ":" + String(skajwl).padStart(2, "0");

  return value;
}

function solution(video_len, pos, op_start, op_end, commands) {
  var answer = "";
  let len = video_len.split(":");
  len = formatted(len);
  let current = pos.split(":");
  current = formatted(current);
  let start = op_start.split(":");
  start = formatted(start);
  let end = op_end.split(":");
  end = formatted(end);

  for (let i = 0; i < commands.length; i++) {
    let item = commands[i];

    if (current >= start && current <= end) {
      current = end;
    }

    if (item === "next") {
      current = Math.min(current + 10, len);
    }
    if (item === "prev") {
      current = Math.max(current - 10, 0);
    }

    if (current >= start && current <= end) {
      current = end;
    }
  }

  answer = reformat(current);

  return answer;
}
