// 시간초과

function solution(maps) {
  var n = maps.length;
  var m = maps[0].length;
  var q = [[0, 0, 1]];
  var direction = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  while (q.length > 0) {
    let [i, j, c] = q.shift();
    maps[i][j] = 0;
    if (i == n - 1 && j == m - 1) {
      return c;
    }
    for (d of direction) {
      if (maps[i + d[0]] && maps[i + d[0]][j + d[1]]) {
        q.push([i + d[0], j + d[1], c + 1]);
      }
    }
  }
  return -1;
}
