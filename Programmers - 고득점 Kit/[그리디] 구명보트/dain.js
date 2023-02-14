function solution(people, limit) {
  var answer = 0;
  let a = 0;
  let i = people.length - 1;
  people.sort((a, b) => a - b);
  while (people.length > 0) {
    answer += 1;
    a = people.pop();
    if (limit - a >= people[0]) {
      for (i; i >= 0; i--) {
        if (people[i] <= limit - a) {
          people.splice(i, 1);
          break;
        }
      }
    }
  }
  return answer;
}
