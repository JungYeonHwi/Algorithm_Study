function solution(str_list) {
  var answer = [];

  let l = str_list.indexOf("l");
  let r = str_list.indexOf("r");

  if (l === -1 && r === -1) answer = [];
  else if (l === -1 && r > -1) {
    answer = str_list.filter((item, index) => index > r);
  } else if (l > -1 && r === -1) {
    answer = str_list.filter((item, index) => index < l);
  } else {
    if (l < r) answer = str_list.filter((item, index) => index < l);
    else answer = str_list.filter((item, index) => index > r);
  }

  return answer;
}
