function solution(people, limit) {
  var answer = 0;
  people.sort((a, b) => a - b);
  while (people.length > 0) {
    answer += 1;
    let a = people.pop();
    if (limit - a >= people[0]) {
      for (let i = 0; i < people.length; i++) {
        if (people[i] <= limit - a) {
          people.splice(i, 1);
          break;
        }
      }
    }
  }
  return answer;
}
